# st08_file_upload.py — 8장 : 파일 올리고 내려받기
import io
import pandas as pd
import streamlit as st

st.title("CSV 분석기")
st.caption("CSV 파일을 올리면 요약 통계와 그래프를 보여 줍니다. (실습: data/titanic.csv)")

file = st.file_uploader("CSV 파일 선택", type=["csv"])
if file is None:
    st.info("왼쪽 위 'Browse files' 로 파일을 올려 주세요.")
    st.stop()                                   # 아래 코드는 실행하지 않음

df = pd.read_csv(file)
st.success(f"{file.name} : {df.shape[0]}행 × {df.shape[1]}열")
st.dataframe(df.head())

num_cols = df.select_dtypes("number").columns.tolist()
col = st.selectbox("분석할 숫자 열", num_cols)
st.write(df[col].describe())
st.bar_chart(df[col].value_counts().sort_index())

# 결과 내려받기
summary = df.describe().T
buf = io.StringIO(); summary.to_csv(buf)
st.download_button("요약 통계 CSV 내려받기", buf.getvalue().encode("utf-8-sig"),
                   file_name="summary.csv", mime="text/csv")
