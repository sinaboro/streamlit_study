# pages_demo/Home.py — 9장 : 여러 페이지 앱 (실행: streamlit run pages_demo/Home.py)
# 같은 폴더의 pages/ 안에 있는 .py 파일이 자동으로 왼쪽 메뉴에 페이지로 추가됩니다.
import streamlit as st

st.set_page_config(page_title="멀티페이지 데모", page_icon="🏠")
st.title("🏠 홈")
st.write("왼쪽 사이드바에서 페이지를 고르세요.")

if "nickname" not in st.session_state:
    st.session_state.nickname = "손님"
st.session_state.nickname = st.text_input("닉네임 (다른 페이지에서도 유지됨)", st.session_state.nickname)
