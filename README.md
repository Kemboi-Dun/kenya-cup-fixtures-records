# Kenya Cup Fixtures

> [!NOTE]
> Data displayed are fetched from a different site.
> [Data source page](https://www.kenyacup.co.ke/upcoming/kenyacup/)

![Screenshot from 2024-07-09 18-00-47](https://github.com/Kemboi-Dun/kenya-cup-fixtures-records/assets/86706504/41ebc2fd-7c84-4534-9944-a54fe30078aa)

## Backend Setup
```
git clone git@github.com:Kemboi-Dun/kenya-cup-fixtures-records.git
```
```
cd kenya-cup-fixtures-backend
```
```
pip install fastapi uvicorn requests beautifulsoup4

```
```
 fastapi dev Extract-Fixtures.py
```

## Frontend Setup
```
git clone git@github.com:Kemboi-Dun/kenya-cup-fixtures-records.git
```
```
npm install
```
```
npm run dev
```

# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules:

- Configure the top-level `parserOptions` property like this:

```js
export default {
  // other rules...
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
    project: ['./tsconfig.json', './tsconfig.node.json'],
    tsconfigRootDir: __dirname,
  },
}
```

- Replace `plugin:@typescript-eslint/recommended` to `plugin:@typescript-eslint/recommended-type-checked` or `plugin:@typescript-eslint/strict-type-checked`
- Optionally add `plugin:@typescript-eslint/stylistic-type-checked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and add `plugin:react/recommended` & `plugin:react/jsx-runtime` to the `extends` list
