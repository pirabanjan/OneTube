import base64
import time
# import hydralit_components as hc
import streamlit as st
import requests
import subprocess
import sys
import json
import numpy as np
import requests


# import hydralit_components as hc
# import time

# API request.
def fetch(session, url):
    try:
        result = session.get(url)
        return result.json()
    except Exception:
        return {}


# Background Gif of the application
def bg():
    # side_bg_ext = 'gif'
    file_ = open(r"C:\Users\DELL\PycharmProjects\pythonProject\FrontEnd\gif\Left-Right-Brain-Signals.webp", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
        f"""
      <style>

       [class="stApp css-ffhzg2 eczokvf1"] {{
            background: url(data:image/gif;base64,{data_url});
            background-size: cover;
      }}
      </style>
      """,
        unsafe_allow_html=True,
    )


# background audio for the home page.
def autoplay_audio():
    with open(r"C:\Users\DELL\PycharmProjects\pythonProject\FrontEnd\Sound\test.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay class="stAudio" loop="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


def main():
    st.set_page_config(
        page_title="Cyber-safety",
        page_icon="🤖"
    )
    bg()
    autoplay_audio()
    st.title("Welcome to Cyber-safety")
    st.sidebar.success("Select a page above")
    session = requests.Session()
    with st.form("my_form"):
        index = st.number_input("ID", min_value=0, max_value=100, key="index")
        # index = st.text_input("Input a text")

        submitted = st.form_submit_button("Submit")

        # if submitted:
        #     my_bar = st.progress(0)
        #     for percent_complete in range(10):
        #         time.sleep(0.1)
        #         my_bar.progress(percent_complete + 1)
        #     # st.write("Result")
        #     url = 'https://z0ml9n8tn8.execute-api.us-east-1.amazonaws.com'
        #     myobj = {'text': 'somevalue'}
        #     x = requests.post(url, data=myobj)
        #     print(x)
        #     if x:
        #         st.text(x.text)
        #     else:
        #         st.error("Error")


if __name__ == '__main__':
    main()
