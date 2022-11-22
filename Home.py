import pandas
import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Joseph Tefera")
    content = """
    Hi, My name is Joseph Tefera. I am an aspiring python programmer. I am a Financial Technology
    major in VCU minoring in Math and Statistics looking to graduate in May 2023. My IT learning began
    in high school from my coding classes but began to sprout when I started to compete in hackathons
    hosted at my college and at Virginia Tech. I have worked for JB Hunt Logistics as well as 
    Major Leage Hacking fellowship. I still have a lot to learn and I look forward to it.
    
    """
    st.info(content)

content0 = """
Below you can find some of the apps I built while watching a course on Udemy by Ardit. 
Feel free to contact me. #
"""
st.write(content0)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:11].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[11:].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

