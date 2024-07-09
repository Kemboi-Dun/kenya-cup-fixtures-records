import axios from "axios";
import { useEffect, useState } from "react";

function App() {
  const [fixtures, setFixtures] = useState([]);

  const fetch_fixtures = async () => {
    const api_url = "http://127.0.0.1:8000/get_fixtures/";
    try {
      const response = await axios.get(api_url);
      response.status === 200 ? setFixtures(response.data) : setFixtures([]);
    } catch (error) {
      console.error("Error occured fetching fixtures :: ", error);
    }
  };

  useEffect(() => {
    fetch_fixtures();
  }, []);

  return (
    <div className="fixtures-body-container">
      <div className="fixtures-wrapper">
        <header className="fixtures-header">
          <h1>Kenya Cup Fixtures</h1>
          <img
            src="https://upload.wikimedia.org/wikipedia/en/7/7a/Kenya_Cup_logo.png"
            alt="Kenya_Cup_logo"
          />
        </header>

        <ul className="fixtures-container">
          {fixtures?.map((fixture: any, index: any) => (
            <li className="fixture-wrapper" key={index}>
              {fixture.Match_title && (
                <h3 className="fixture-match-title">{fixture.Match_title}</h3>
              )}

              <span className="fixture-month">{fixture.Match_day}</span>

              <p className="fixture-date">{fixture.Match_date}</p>
              {fixture.Final_title && (
                <h4 className="fixture-category">{fixture.Final_title}</h4>
              )}
              {fixture.teams?.map((team: any, index: any) => (
                <a
                  href="https://www.kenyacup.co.ke/upcoming/kenyacup/"
                  target="_blank"
                  key={index}
                  
                >
                  <div className="fixture-matches">
                    <p className="fixture-team">{team.team_A}</p>
                    <div className="fixture-results-wrapper">
                      <p className="fixture-results">
                        {team.team_A_result} - {team.team_B_result}
                      </p>
                      <span className="fixture-game-period">FT</span>
                    </div>
                    <p className="fixture-team">{team.team_B}</p>
                  </div>
                </a>
              ))}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
