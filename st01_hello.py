# st01_hello.py — 1장 : 첫 Streamlit 앱
# 실행: streamlit run st01_hello.py
import streamlit as st

st.title("안녕하세요, Streamlit! 👋")
st.write("파이썬 파일 하나로 웹 앱을 만듭니다.")

name = st.text_input("이름을 입력하세요", "홍길동")
st.write(f"반갑습니다, **{name}** 님!")

if st.button("풍선 날리기"):
    st.balloons()
