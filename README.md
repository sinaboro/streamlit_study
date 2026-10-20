# Streamlit Study — 파이썬 코드로 웹 앱 만들기

「YOLO와 ChatGPT를 활용한 생성형 AI 어플리케이션 개발」 과정의 **Streamlit 기초** 학습 자료입니다.
교안(PDF)과 교안에 나오는 예제 앱 소스가 함께 들어 있습니다.

📘 **교안** : [docs/Streamlit_기초_학습교안.pdf](docs/Streamlit_기초_학습교안.pdf) (44쪽)

교안의 [실습 코드] 상자는 이 저장소의 파일과 내용이 같고, 교안의 그림은 이 코드를 실제로 실행한 화면입니다.

---

## 1. 시작하기

### 준비물
- Python 3.10 이상
- VS Code (또는 명령 프롬프트)

### 설치

```bash
git clone https://github.com/sinaboro/streamlit_study.git
cd streamlit_study
pip install -r requirements.txt
```

### 실행

```bash
streamlit run st01_hello.py
```

브라우저가 자동으로 열리고 주소는 `http://localhost:8501` 입니다. 끝낼 때는 터미널에서 **Ctrl + C** 를 누릅니다.

> ⚠️ `python st01_hello.py` 가 아니라 **`streamlit run 파일이름.py`** 로 실행해야 합니다.

---

## 2. 학습 순서

| 장 | 주제 | 예제 파일 | 배우는 것 |
| --- | --- | --- | --- |
| 1 | Streamlit 시작하기 | `st01_hello.py` | 설치 · 실행 · 재실행 원리 |
| 2 | 글자와 숫자 보여 주기 | `st02_text.py` | title · markdown · write · metric · 알림 상자 |
| 3 | 입력 위젯 | `st03_widgets.py` | button · slider · selectbox · checkbox … |
| 4 | 화면 배치하기 | `st04_layout.py` | sidebar · columns · tabs · expander · form |
| 5 | 표와 차트 | `st05_data_chart.py` | dataframe · data_editor · bar_chart · pyplot |
| 6 | 상태 기억하기 | `st06_session_state.py` | session_state · 콜백 · key |
| 7 | 캐싱으로 빠르게 | `st07_cache.py` | cache_data · cache_resource |
| 8 | 파일 올리고 내려받기 | `st08_file_upload.py` | file_uploader · stop · download_button |
| 9 | 여러 페이지 앱 | `pages_demo/` | pages 폴더 · 페이지 간 상태 공유 |
| 10 | 채팅 앱과 ChatGPT | `st10_chatbot.py` | chat_message · chat_input · secrets |
| 11 | 미니 프로젝트 | `st11_dashboard.py`, `st12_text_analyzer.py` | 타이타닉 대시보드 · TF-IDF 문장 유사도 |
| 12 | 인터넷에 배포하기 | — | requirements.txt · Streamlit Community Cloud |

9장 여러 페이지 앱은 이렇게 실행합니다.

```bash
streamlit run pages_demo/Home.py
```

---

## 3. 폴더 구조

```
streamlit_study/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   └── Streamlit_기초_학습교안.pdf     ← 교안
├── data/
│   └── titanic.csv                     ← 타이타닉 승객 891명 (5 · 7 · 8 · 11장)
├── st01_hello.py ~ st12_text_analyzer.py
└── pages_demo/
    ├── Home.py
    └── pages/
        ├── 1_계산기.py
        └── 2_소개.py
```

---

## 4. ChatGPT 연결하기 (10장)

키가 없으면 `st10_chatbot.py` 는 **따라 말하기 봇**으로 동작합니다. ChatGPT 와 대화하려면:

```bash
pip install openai
```

프로젝트 폴더에 `.streamlit/secrets.toml` 파일을 만들고 키를 넣습니다.

```toml
OPENAI_API_KEY = "sk-..."
```

> 🔒 **API 키는 절대 코드에 직접 쓰거나 GitHub 에 올리지 마세요.**
> `.streamlit/secrets.toml` 은 `.gitignore` 에 들어 있어 커밋되지 않습니다.
> 배포할 때는 Streamlit Community Cloud 앱 설정의 **Secrets** 칸에 입력합니다.

---

## 5. 확인 환경

모든 예제는 아래 환경에서 실행해 확인했습니다. (Windows)

- Python 3.12
- Streamlit 1.66
- pandas 3.0 · matplotlib 3.11 · scikit-learn 1.9

> 10장의 ChatGPT 모드는 API 키가 필요해 따로 실행해 확인하지 않았습니다(키 없이 동작하는 따라 말하기 모드는 확인함).

---

## 참고 자료

- Streamlit 공식 문서 : https://docs.streamlit.io
- Streamlit 갤러리 : https://streamlit.io/gallery
- Streamlit Community Cloud : https://share.streamlit.io
