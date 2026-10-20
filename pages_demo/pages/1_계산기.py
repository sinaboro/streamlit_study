import streamlit as st

st.title("🧮 계산기")
st.write(f"{st.session_state.get('nickname', '손님')} 님, 숫자 두 개를 입력하세요.")
a = st.number_input("A", value=3)
b = st.number_input("B", value=4)
op = st.radio("연산", ["+", "-", "×", "÷"], horizontal=True)
res = {"+": a + b, "-": a - b, "×": a * b, "÷": a / b if b else float("nan")}[op]
st.metric("결과", res)
