# st06_session_state.py — 6장 : 상태 기억하기 (session_state)
import streamlit as st

st.title("session_state 로 값 기억하기")

# ❌ 잘못된 카운터 : 버튼을 누를 때마다 파일 전체가 다시 실행되어 0으로 돌아감
count_wrong = 0
if st.button("잘못된 +1"):
    count_wrong += 1
st.write("잘못된 카운터:", count_wrong)

st.divider()

# ✅ 올바른 카운터 : session_state 는 재실행되어도 값이 남아 있음
if "count" not in st.session_state:
    st.session_state.count = 0

col1, col2 = st.columns(2)
if col1.button("+1"):
    st.session_state.count += 1
if col2.button("초기화"):
    st.session_state.count = 0
st.metric("올바른 카운터", st.session_state.count)

st.divider()

# 콜백(on_click) + 위젯 key 로 할 일 목록 만들기
if "todos" not in st.session_state:
    st.session_state.todos = []

def add_todo():
    text = st.session_state.new_todo.strip()
    if text:
        st.session_state.todos.append(text)
    st.session_state.new_todo = ""          # 입력창 비우기

st.text_input("할 일", key="new_todo")
st.button("추가", on_click=add_todo)
for i, t in enumerate(st.session_state.todos, 1):
    st.write(f"{i}. {t}")
