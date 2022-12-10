import base64
import streamlit as st
from PIL import Image


def bg():
    # side_bg_ext = 'gif'
    file_ = open(r"C:\Users\DELL\PycharmProjects\pythonProject\FrontEnd\gif\giphy (1).gif", "rb")
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
    with open(r"C:\Users\DELL\PycharmProjects\pythonProject\FrontEnd\Sound\motivational-day-112790.mp3", "rb") as f:
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
    bg()
    autoplay_audio()
    st.title("About US")
    st.text("GitHub")

    st.header("Group Members")

    col1, col2, col3, col4, col5 = st.columns(5)

    praba = Image.open(r'C:\Users\DELL\PycharmProjects\pythonProject\FrontEnd\Images\Pirabanjan.jpg')
    api = Image.open(r'C:\Users\DELL\PycharmProjects\pythonProject\FrontEnd\Images\api.jpeg')

    with col1:
        st.image(api)
        st.write('Apinya: [LinkedIn](https://www.linkedin.com/in/apinya-t/)')
    with col2:
        st.image(praba)
        st.write('Pirabanjan: [LinkedIn](https://www.linkedin.com/in/pirabanjan-kirupaharan/)')
    with col3:
        st.text("Sarah: LinkedIn")
        st.write('Sarah: [LinkedIn](https://www.linkedin.com/in/pirabanjan-kirupaharan/)')
    with col4:
        st.text("Dharshana: LinkedIn")
        st.write('Dharshana: [LinkedIn](https://www.linkedin.com/in/pirabanjan-kirupaharan/)')
    with col5:
        st.text('Kiranvir: LinkedIn')
        st.write('Dharshana: [LinkedIn](https://www.linkedin.com/in/pirabanjan-kirupaharan/)')


if __name__ == '__main__':
    main()
