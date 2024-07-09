import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_credentials = True,   
)

#site user-agent to handle Mod-security error
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

url = "https://www.kenyacup.co.ke/upcoming/kenyacup/" #site URL

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# function to extract fixtures
def extract_fixtures(soup):
    cards= []
   
    
    fixture_cards = soup.find('main', id='content').find('div', class_='mg-card-box').findAll('p')
    for fixture_card in fixture_cards:
        card_details = fixture_card.text.strip()
        if card_details:
            card_list = card_details.split('\n')
            
            if card_list:
                card_info = parse_card(card_list)
                if card_info:
                    cards.append(card_info)

    return cards


# parse card
def parse_card(cards):
    card = {}
    teams_run = []
    
    try:
        title_selection = cards[0].split('|')
        if len(title_selection) == 3:
            card["Match_title"] = title_selection[0]
            card["Match_day"] = title_selection[1]
        else:
            card["Match_day"] = title_selection[0]
       
        card["Match_date"] = title_selection[-1]
        
        for line in cards[1:]:
            teams={}
            if '-' not in line.strip():
                team_selection = line.strip().split('–')
            else:
                team_selection = line.strip().split('-')
            team_one_info = team_selection[0].split()
            if team_one_info[0].lower().startswith('final'):
                card["Final_title"] = team_one_info[0]
                team_name = " ".join(team_one_info[:-1])
                teams["team_A"] = team_name.replace('Final', '').strip()       
            else:
                teams["team_A"] = " ".join(team_one_info[:-1])
            teams["team_A_result"]=team_one_info[-1]
            team_two_info= team_selection[-1].split()
            teams["team_B"] = " ".join(team_two_info[1:])
            teams["team_B_result"]=team_two_info[0]
                
            teams_run.append(teams)
            
        card["teams"]=teams_run
            
    except Exception as e:
        print(f"Error parsing card :: {e}")
        return None
    return card


@app.get("/get_fixtures/")
async def get_fixtures():
    fixtures = extract_fixtures(soup)
    return JSONResponse(content = fixtures)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)