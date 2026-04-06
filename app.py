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
    if("youtu.be/" in url):
        split1 = url.split("youtu.be/")[1]
        split2 = split1.split("?")[0]
        return split2
    else:
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
    words = transcript.split()
    for i in range(0,len(words),chunk_Size):
        yield " ".join(words[i:i+chunk_Size])
    pass

st.title("Youtube Summarizer")
st.write("Please make sure the video is not more than 20 mins long as it might not give any results: ")
url = st.text_input("Paste your youtube link here: ")
if st.button("Summazrise"):
    try:
        extract = extract_videoId(url)
        transcript = get_transcript(extract)
        summaries = []
        chunks = chunk_transcript(transcript)
        for chunk in chunks:
            chunk_summary = summarize(chunk)
            summaries.append(chunk_summary)

        final = summarize(" ".join(summaries))
        st.write(final)
    except Exception as e :
        st.write("Oh no! Only english is supported for now! Summaries for other Languages is under work...")
