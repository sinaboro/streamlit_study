# st05_data_chart.py — 5장 : 표와 차트
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

DATA = Path(__file__).parent / "data" / "titanic.csv"
plt.rc("font", family="Malgun Gothic"); plt.rcParams["axes.unicode_minus"] = False

st.title("타이타닉 데이터 살펴보기")
df = pd.read_csv(DATA)

st.subheader("1. 표 : st.dataframe")
st.dataframe(df.head(10), width="stretch")

st.subheader("2. 요약 숫자 : st.metric")
c1, c2, c3 = st.columns(3)
c1.metric("승객 수", f"{len(df):,}명")
c2.metric("생존율", f"{df['survived'].mean():.1%}")
c3.metric("평균 나이", f"{df['age'].mean():.1f}세")

st.subheader("3. Streamlit 기본 차트")
by_class = df.groupby("class")["survived"].mean().rename("생존율")
st.bar_chart(by_class)

rng = np.random.default_rng(0)
st.line_chart(pd.DataFrame(rng.normal(size=(30, 2)).cumsum(0), columns=["A", "B"]))

st.subheader("4. matplotlib 그림 : st.pyplot")
fig, ax = plt.subplots(figsize=(6, 3))
df["age"].dropna().plot.hist(bins=20, ax=ax, color="#1f77b4")
ax.set_title("나이 분포"); ax.set_xlabel("나이")
st.pyplot(fig)

st.subheader("5. 표 직접 고치기 : st.data_editor")
edited = st.data_editor(pd.DataFrame({"과목": ["국어", "수학"], "점수": [80, 90]}), num_rows="dynamic")
st.write("평균 점수:", edited["점수"].mean())
