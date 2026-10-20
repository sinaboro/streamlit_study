# st04_layout.py — 4장 : 화면 배치 (sidebar · columns · tabs · expander · form)
import streamlit as st

st.set_page_config(page_title="레이아웃 연습", page_icon="🧩", layout="wide")
st.title("레이아웃 연습")

# 1) 사이드바
with st.sidebar:
    st.header("설정")
    color = st.selectbox("테마 색", ["파랑", "초록", "빨강"])
    size = st.slider("글자 크기", 10, 40, 20)

# 2) 열 나누기 (비율 2:1)
left, right = st.columns([2, 1])
left.subheader("왼쪽 넓은 칸")
left.write(f"선택한 색: {color}, 크기: {size}")
right.subheader("오른쪽 좁은 칸")
right.button("오른쪽 버튼")

# 3) 탭
tab1, tab2 = st.tabs(["📈 차트", "📋 표"])
with tab1:
    st.line_chart([1, 3, 2, 5, 4])
with tab2:
    st.table({"이름": ["가", "나"], "점수": [90, 85]})

# 4) 접었다 펴기
with st.expander("자세히 보기"):
    st.write("평소에는 숨겨 두고 필요할 때 펼쳐 보는 영역입니다.")

# 5) 폼 : 제출 버튼을 누를 때만 한 번에 실행
with st.form("login"):
    uid = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")
    ok = st.form_submit_button("로그인")
if ok:
    st.write(f"{uid} 님 로그인 시도 (비밀번호 {len(pw)}자리)")
