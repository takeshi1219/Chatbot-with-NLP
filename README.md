# NLP Chatbot

A conversational AI chatbot built with Flask and ChatterBot. The bot uses natural language processing to understand and respond to user messages.

## Features

- 💬 Real-time chat interface
- 🤖 NLP-powered responses using ChatterBot
- 📚 Trained on English conversation corpus
- 🎨 Clean, modern UI

## Tech Stack

- **Backend:** Flask, ChatterBot
- **NLP:** NLTK
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript

## Local Development

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Chatbot-with-NLP
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download NLTK data:
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('averaged_perceptron_tagger'); nltk.download('averaged_perceptron_tagger_eng'); nltk.download('stopwords')"
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and go to: http://127.0.0.1:5000/chatbot

## Deployment

### Deploy to Render (Recommended - Free)

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and sign up
3. Click **New** → **Web Service**
4. Connect your GitHub repository
5. Configure:
   - **Name:** chatbot-nlp
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt && python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('averaged_perceptron_tagger'); nltk.download('averaged_perceptron_tagger_eng'); nltk.download('stopwords'); nltk.download('wordnet')"`
   - **Start Command:** `gunicorn wsgi:app`
6. Click **Create Web Service**

### Deploy to Railway

1. Push your code to GitHub
2. Go to [railway.app](https://railway.app)
3. Click **New Project** → **Deploy from GitHub repo**
4. Select your repository
5. Railway will auto-detect the Procfile and deploy

### Deploy to Heroku

1. Install Heroku CLI
2. Run:
```bash
heroku login
heroku create your-chatbot-name
git push heroku main
```

## Project Structure

```
Chatbot-with-NLP/
├── app.py              # Flask application
├── chatbot.py          # ChatterBot setup & training
├── wsgi.py             # WSGI entry point for production
├── requirements.txt    # Python dependencies
├── Procfile            # Process file for deployment
├── runtime.txt         # Python version
├── render.yaml         # Render deployment config
├── nltk.txt            # NLTK packages to download
├── templates/
│   └── index.html      # Chat UI
├── static/
│   └── styles/
│       └── style.css   # Styling
└── db.sqlite3          # SQLite database (trained data)
```

## Screenshots

![Conversation](chat2.png)

## License

MIT License
