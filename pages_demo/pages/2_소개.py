import streamlit as st

st.title("ℹ️ 소개")
st.markdown("""
- 이 앱은 **pages/** 폴더 방식의 멀티페이지 예제입니다.
- 파일 이름 앞의 숫자(1_, 2_)로 메뉴 순서를 정합니다.
- `st.session_state` 값은 페이지를 옮겨도 유지됩니다.
""")
st.write("현재 닉네임:", st.session_state.get("nickname", "손님"))
