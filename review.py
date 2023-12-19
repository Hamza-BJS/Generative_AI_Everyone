import openai
import streamlit as st
from pathlib import Path
import configparser

with st.sidebar:
       keys = st.text_input("Enter your OpenAI API key")

openai.api_key = keys
def get_response_from_chatgpt(text):
    prompt= f"Identify and return the sentiment either positive or negative in given text. text: {text}"
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-1106",
    messages=[
                {"role": "system", "content": "You are a helpful Text Sentiment Analyzer That returns One Word Sentiment."},
                {"role": "user", "content":prompt }
        ],
        temperature = 0.1
        )
    sentiment = response['choices'][0]['message']['content']
    return sentiment



st.title("ChatGPT Text Sentiment Analyzer")
model="gpt-3.5-turbo"
text = st.text_input("Enter Text", value="I like pizza")

if st.button("Submit"):
    with st.spinner("Openai is processing"):
        sentiment = get_response_from_chatgpt(text)
        st.success("Completed Successfully")

    st.write(f"Sentiment: {sentiment}")
    