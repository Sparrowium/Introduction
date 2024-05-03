import streamlit as st

st.set_page_config(page_title="Welcome")

with st.container():
    st.write("Hi, My name is Minh Pham")
    st.write("Am a student from US")
    st.write("I am passionate about findings news stuff to learn and utilize Python to be more professionally")

with st.container():
    st.write("------------------------------------------------")
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("What I do")
        st.write("##")
        st.write("On my github pages I am developing softwares and webpages")
