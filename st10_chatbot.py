# st10_chatbot.py — 10장 : 채팅 화면과 ChatGPT 연결
# OpenAI 키가 없으면 '따라 말하기' 봇으로 동작합니다.
# 키 설정 : .streamlit/secrets.toml 에  OPENAI_API_KEY = "sk-..."   (깃허브에 올리지 말 것!)
import streamlit as st

st.title("💬 나의 첫 챗봇")

try:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    api_key = None
mode = "ChatGPT" if api_key else "따라 말하기(키 없음)"
st.caption(f"현재 모드: {mode}")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "안녕하세요! 무엇이든 물어보세요."}]

for m in st.session_state.messages:                 # 지난 대화 다시 그리기
    with st.chat_message(m["role"]):
        st.write(m["content"])

def ask_gpt(messages):
    from openai import OpenAI                         # pip install openai
    client = OpenAI(api_key=api_key)
    res = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return res.choices[0].message.content

if prompt := st.chat_input("메시지를 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        answer = ask_gpt(st.session_state.messages) if api_key else f"'{prompt}' 라고 하셨군요! 🦜"
        st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
