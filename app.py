import os
from groq import Groq
from dotenv import load_dotenv
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_transcript(video_id):
    ytt = YouTubeTranscriptApi()
    transcript=ytt.fetch(video_id)
    text = [item.text for item in transcript]
    script=" ".join(text)
    return script

def extract_videoId(url):
    return url.split("v=")[1]

def summarize(transcript):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": "summarize this: " + transcript}
        ]
    )
    return response.choices[0].message.content


def chunk_transcript(transcript, chunk_Size=1000):
    for i in range(len(transcript),chunk_Size):
        yield transcript[i:i+chunk_Size]

st.title("Yotube summarizer")
url = st.text_input("Enter ur yt url here")
if st.button("Summarize"):
    try:
      extract = extract_videoId(url)
      transcript = get_transcript(extract)
      summary = summarize(transcript)
      st.write(summary)
    except Exception as e:
        st.error("Couldn't fetch transcript.Try an English video! ")