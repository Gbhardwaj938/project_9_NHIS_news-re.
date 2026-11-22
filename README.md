
# AI-Powered News Research Tool

A Streamlit application that retrieves recent articles through NewsAPI and uses an OpenAI model through LangChain to create a structured business/equity news research brief.

## Features

- Search news by company, industry, stock, or topic.
- Fetch article metadata from NewsAPI.
- Generate an AI-assisted summary with LangChain + OpenAI.
- Display article title, publisher, publication date, description, and original URL.
- Export fetched article metadata to CSV.
- Keep recent search terms during the current app session.
- Store credentials in a local `.env` file (not in source code).

## Technology stack

Python, Streamlit, NewsAPI, LangChain, langchain-openai, OpenAI API, Pandas.

## Project structure

```text
News_Research_Tool/
├── app.py
├── news_api.py
├── langchain_config.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── data/
├── outputs/
├── assets/
└── .streamlit/config.toml
```

## Requirements

- Python 3.10 or newer.
- OpenAI API key with API billing/usage enabled as applicable.
- NewsAPI key. Check the current NewsAPI plan, request limits, and developer-plan restrictions.

## Setup in VS Code (Windows PowerShell)

Open the project folder in VS Code. Open **Terminal → New Terminal**, then run:

### 1. Create a virtual environment

```powershell
py -m venv .venv
```

### 2. Activate it

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

Or run the commands through the environment's Python without activation:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Upgrade pip and install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Create your environment file

In the project root, copy `.env.example` to a new file named `.env`.

PowerShell:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace the placeholder values:

```env
OPENAI_API_KEY=your_real_openai_api_key
NEWSAPI_KEY=your_real_newsapi_key
OPENAI_MODEL=gpt-4o-mini
```

Do not add quotes unless required by your key format. Never commit or share `.env`.

### 5. Run the app

```powershell
streamlit run app.py
```

Streamlit will show a local URL, usually `http://localhost:8501`. Open it in your browser.

## How to use

1. Enter a company, industry, stock, or topic in the search box.
2. Select the language, sort order, and article count in the sidebar.
3. Click **Search news and summarize**.
4. Read the AI research brief and open original articles to verify details.
5. Use **Download articles as CSV** to export article metadata.

## API key setup

- OpenAI: create an API key in the OpenAI developer platform. API usage is billed separately from a ChatGPT subscription; review current API pricing and billing before use.
- NewsAPI: create an account and copy the API key from the NewsAPI dashboard. Check the current plan restrictions, daily request limits, and whether your intended use is permitted.

Official documentation:
- OpenAI API keys and SDKs: https://developers.openai.com/api/docs/libraries
- OpenAI pricing: https://openai.com/api/pricing/
- LangChain OpenAI integration: https://docs.langchain.com/oss/python/integrations/chat/openai
- NewsAPI Python client: https://newsapi.org/docs/client-libraries/python
- NewsAPI Everything endpoint: https://newsapi.org/docs/endpoints/everything

## Git and GitHub commands

Run these commands from the project folder:

```powershell
git init
git status
git add .
git status
git commit -m "Initial commit: AI News Research Tool"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/News_Research_Tool.git
git push -u origin main
```

Replace the remote URL with your own GitHub repository URL. If Git asks you to authenticate, complete the GitHub sign-in flow.

Before committing, confirm `.env` is not listed by:

```powershell
git status
```

If `.env` was accidentally committed, rotate/revoke the exposed keys immediately; removing the file in a later commit does not make an exposed key safe.

## Troubleshooting

- **`ModuleNotFoundError`**: activate `.venv`, then run `pip install -r requirements.txt`.
- **`NEWSAPI_KEY is missing`**: check that `.env` is in the same folder as `app.py`, and that the variable name is exact.
- **NewsAPI error / no results**: check the key, query spelling, language, date window, and your NewsAPI plan limits.
- **OpenAI authentication or quota error**: verify the key and API billing/usage limits. ChatGPT Plus/Free subscriptions do not automatically include API credits.
- **Streamlit command not found**: run `python -m streamlit run app.py`.
- **Wrong Python interpreter**: in VS Code press `Ctrl+Shift+P` → `Python: Select Interpreter` → select `.venv`.

## Limitations and responsible use

- NewsAPI returns article metadata and descriptions; the app does not guarantee access to full article text.
- Search results and availability depend on NewsAPI plan restrictions and publisher coverage.
- AI summaries can make mistakes. Always open the original sources and verify important claims.
- This is an educational research assistant, not financial, legal, or investment advice.
- Do not paste private credentials into source files, notebooks, screenshots, or public repositories.
