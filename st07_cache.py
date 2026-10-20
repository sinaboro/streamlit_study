# st07_cache.py — 7장 : 캐싱으로 빠르게
import time
from pathlib import Path
import pandas as pd
import streamlit as st

DATA = Path(__file__).parent / "data" / "titanic.csv"
st.title("st.cache_data 효과 보기")

@st.cache_data                      # 같은 인자로 다시 부르면 저장된 결과를 바로 돌려줌
def load_data(path):
    time.sleep(2)                   # 오래 걸리는 작업(큰 파일, DB 조회)을 흉내
    return pd.read_csv(path)

start = time.time()
df = load_data(DATA)
st.write(f"불러오기 시간: **{time.time() - start:.2f}초** (처음 2초, 다음부터 거의 0초)")
st.dataframe(df.head())

if st.button("다시 실행해 보기"):
    st.rerun()
if st.button("캐시 비우기"):
    load_data.clear()
    st.rerun()
