# st11_dashboard.py — 11장 미니 프로젝트 ① : 타이타닉 대시보드
from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="타이타닉 대시보드", page_icon="🚢", layout="wide")
DATA = Path(__file__).parent / "data" / "titanic.csv"

@st.cache_data
def load():
    return pd.read_csv(DATA)

df = load()

with st.sidebar:
    st.header("🔎 필터")
    sex = st.multiselect("성별", ["male", "female"], default=["male", "female"])
    pclass = st.multiselect("객실 등급", [1, 2, 3], default=[1, 2, 3])
    age = st.slider("나이 범위", 0, 80, (0, 80))

# 나이를 모르는 승객(177명)은 나이 조건과 상관없이 포함
f = df[df["sex"].isin(sex) & df["pclass"].isin(pclass) & (df["age"].between(*age) | df["age"].isna())]

st.title("🚢 타이타닉 생존 대시보드")
c1, c2, c3, c4 = st.columns(4)
c1.metric("선택된 승객", f"{len(f):,}명")
c2.metric("생존자", f"{int(f['survived'].sum()):,}명")
c3.metric("생존율", f"{f['survived'].mean():.1%}" if len(f) else "-")
c4.metric("평균 요금", f"${f['fare'].mean():.1f}" if len(f) else "-")

left, right = st.columns(2)
with left:
    st.subheader("성별 생존율")
    st.bar_chart(f.groupby("sex")["survived"].mean())
with right:
    st.subheader("객실 등급별 생존율")
    st.bar_chart(f.groupby("pclass")["survived"].mean())

with st.expander("선택된 데이터 보기"):
    st.dataframe(f, width="stretch")
