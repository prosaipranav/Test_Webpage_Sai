import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="MY WEBPAGE",page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")

#-- LOAD ASSETS --
lottie_coding=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
brawl_stars_img=Image.open("images/brawlstars.jpg")


#-- HEADER SECTION --
with st.container():
    st.subheader("Hi,I am Saipranav :wave:")
    st.title("A Student from Abu Dhabi")
    st.write("I am passionate about finding ways to use Python to be more efficient and effective in Webpage development.")
    st.write("[Learn more](https://www.dunesinternationalschool.com/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("WHAT I DO")
        #st.write("#")
        st.write(
            """
            hello my name is Saipranav.i do a lot of things:
            - Coding
            - Play chess
            - Study for CBSE Boards
            """)

    with right_column:
        st.lottie(lottie_coding,height=300, key="coding")

#-- projects -- 
with st.container():
    st.write("---")
    st.header("my projects")
    st.write("##")
    image_column,text_column= st.columns((1,2))        
    with image_column:
        st.image(brawl_stars_img)
    with text_column:
        st.subheader("Brawl Stars")
        st.write(
            """
            Fast-paced 3v3 multiplayer and battle royale made for mobile! Play with friends or solo across a variety of game modes in under three minutes.
            """
        )
        st.markdown("[Watch video...](https://www.youtube.com/@BrawlStars/videos)")
#-- CONTACT --
with st.container():
    st.write("---")
    st.header("Get in Touch with Me!")
    st.write("##")

#Change email address
contact_form="""
<form action="https://formsubmit.co/prosaipranav@email.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
	<input type="text" name="name" placeholder="Your name" required>
	<input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
	<button type="submit">send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()