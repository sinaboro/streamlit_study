# st12_text_analyzer.py — 11장 미니 프로젝트 ② : 문장 유사도 분석기 (NLP 수업 연결)
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("📝 문장 유사도 분석기")
st.caption("TF-IDF 로 문장을 벡터로 바꾸고, 코사인 유사도로 가장 비슷한 문장을 찾습니다.")

default = "I like dog\nYou like dog\nI hate bug\nA dog in a dog house is big"
docs = [s for s in st.text_area("문장 목록 (한 줄에 하나)", default, height=130).splitlines() if s.strip()]
query = st.text_input("비교할 문장", "I love my dog")

if docs and query:
    tv = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
    X = tv.fit_transform(docs + [query])
    sims = cosine_similarity(X[-1], X[:-1]).ravel()
    result = pd.DataFrame({"문장": docs, "유사도": sims.round(3)}).sort_values("유사도", ascending=False)

    best = result.iloc[0]
    st.success(f"가장 비슷한 문장: **{best['문장']}** (유사도 {best['유사도']})")
    st.bar_chart(result.set_index("문장")["유사도"])
    with st.expander("TF-IDF 행렬 보기"):
        st.dataframe(pd.DataFrame(X.toarray(), columns=tv.get_feature_names_out(),
                                  index=docs + ["(질문)"]).round(2))
