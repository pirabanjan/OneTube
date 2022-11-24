import streamlit as st

st.set_page_config(
    page_title = "OneTube",
    # page_icon = ""
)

st.title("Welcome to OneTube")
st.sidebar.success("Select a page above")


if "url" not in st.session_state:
    st.session_state['url'] = ""

url = st.text_input("Input a URL here", st.session_state["url"])
submit = st.button("submit")
if submit:
    st.session_state["url"] = url
    st.write("your url is: ", url)

