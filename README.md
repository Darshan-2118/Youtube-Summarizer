# 🎥 YouTube Video Summarizer

An AI-powered web app that summarizes any YouTube video in seconds. Paste a link, click summarize, and get a clean summary — no need to watch the full video.

Built with Python, Streamlit, and Groq's LLaMA 3.3 70B model.

---

## 🚀 Demo

> Paste any YouTube URL → Get an instant AI summary

Supports both URL formats:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`

---

## ✨ Features

- 🔗 Supports both standard and shortened YouTube URLs
- 🧠 Uses LLaMA 3.3 70B via Groq for fast, accurate summaries
- 📄 Handles long videos with transcript chunking
- ⚡ Clean and simple Streamlit UI
- 🌐 English video support

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI |
| Groq API | LLM inference (LLaMA 3.3 70B) |
| youtube-transcript-api | Fetching video transcripts |
| python-dotenv | Managing API keys |

---

## 📦 Installation

**1. Clone the repository**
```bash
git clone https://github.com/Darshan-2118/yt-summarizer
cd yt-summarizer
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up your API key**

Create a `.env` file in the root folder:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key at [console.groq.com](https://console.groq.com)

**5. Run the app**
```bash
streamlit run app.py
```

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Your Groq API key (free at console.groq.com) |

---

## 📁 Project Structure

```
yt-summarizer/
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── .env                # API keys (not pushed to GitHub)
├── .gitignore          # Ignores .env and .venv
└── README.md           # You are here
```

---

## ⚠️ Limitations

- Only supports videos with English transcripts
- Best results on videos under 20 minutes
- Requires an active internet connection

---

## 🙌 Author

**Darshan** — [GitHub](https://github.com/Darshan-2118) · [LinkedIn](https://linkedin.com/in/darshan2118)

---

## 📄 License

MIT License — feel free to use and modify this project.