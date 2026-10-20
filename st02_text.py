# st02_text.py — 2장 : 글자와 숫자 보여 주기
import streamlit as st

st.title("제목 : st.title")
st.header("큰 소제목 : st.header")
st.subheader("작은 소제목 : st.subheader")
st.text("고정폭 텍스트 : st.text")

st.markdown("**굵게**, *기울임*, `코드`, [링크](https://streamlit.io)")
st.markdown("- 목록 1\n- 목록 2")
st.caption("작은 회색 설명 글 : st.caption")

st.code("for i in range(3):\n    print(i)", language="python")
st.latex(r"\hat{y} = ax + b")

st.divider()
st.write("st.write 는 무엇이든 알아서 보여 줍니다 :", 3 + 4, [1, 2, 3], {"a": 1})

col1, col2, col3 = st.columns(3)
col1.metric("기온", "21 °C", "1.2 °C")
col2.metric("습도", "58 %", "-4 %")
col3.metric("방문자", "1,234", "+56")

st.success("성공 메시지")
st.info("안내 메시지")
st.warning("경고 메시지")
st.error("오류 메시지")
