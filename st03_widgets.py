# st03_widgets.py — 3장 : 입력 위젯
import datetime
import streamlit as st

st.title("입력 위젯 모음")

name = st.text_input("이름", placeholder="이름을 입력하세요")
age = st.number_input("나이", min_value=0, max_value=120, value=20, step=1)
score = st.slider("점수", 0, 100, 70)
grade = st.selectbox("학년", ["1학년", "2학년", "3학년"])
gender = st.radio("성별", ["남", "여"], horizontal=True)
hobbies = st.multiselect("취미", ["독서", "운동", "게임", "음악"], default=["독서"])
agree = st.checkbox("개인정보 수집에 동의합니다")
birthday = st.date_input("생일", datetime.date(2005, 1, 1))
memo = st.text_area("자기소개", height=80)

if st.button("제출", type="primary"):
    if not agree:
        st.warning("동의에 체크해 주세요.")
    else:
        st.success(f"{name}({age}세, {grade}, {gender}) 님 제출 완료!")
        st.write("점수:", score, " / 취미:", ", ".join(hobbies), " / 생일:", birthday)
