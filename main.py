import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 연예인 소울메이트 찾기!",
    page_icon="🔮",
    layout="centered",
)

# 커스텀 스타일링 (귀여운 글씨 및 배경 느낌)
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #FF4B4B;
        text-align: center;
        font-weight: bold;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #555555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .mbti-box {
        background-color: #FFF0F5;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #FF69B4;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 메인 타이틀
st.markdown(
    "<h1 class='main-title'>🔮 MBTI 연예인 소울메이트 탐지기 🔮</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='sub-title'>나랑 같은 MBTI를 가진 대단한(?) 연예인은 누구일까?!</p>",
    unsafe_allow_html=True,
)

# MBTI 데이터베이스 (기본 데이터)
mbti_db = {
    "ENFP": {
        "title": "🎉 흥이 넘치는 인간 비타민",
        "celebs": ["BTS RM", "이효리", "싸이", "부승관(세븐틴)", "싸이"],
        "comment": "오늘도 세상의 모든 것에 흥분할 준비가 되어있는 당신! 정리가 좀 안 되면 어때요, 즐거우면 됐지! 🤪",
    },
    "ENTP": {
        "title": "🔥 말싸움 최강자 & 아이디어 폭주족",
        "celebs": ["신동엽", "라미란", "제시", "육성재"],
        "comment": "토론하자고 하면 눈이 반짝이는 당신! 당신의 드립력에 세상이 정신을 못 차립니다. 🧠💥",
    },
    "INFJ": {
        "title": "🔮 통찰력 만렙의 은밀한 예언자",
        "celebs": ["아이유", "태연", "카이(EXO)", "강동원"],
        "comment": "겉으로는 조용하지만 속으로는 우주의 진리를 탐구 중인 당신... 다 알고 계시죠? 🧙‍♂️",
    },
    "INTJ": {
        "title": "♟️ 세상 모든 걸 계획하는 얼음공주/공자",
        "celebs": ["지드래곤", "보아", "에릭(신화)", "이경규"],
        "comment": "당신의 '5년 뒤 계획' 목록에는 지구 정복도 포함되어 있을 것 같네요. 🤖✨",
    },
    "INFP": {
        "title": "☁️ 몽상에 빠진 귀여운 방구석 시인",
        "celebs": ["BTS 슈가", "IU(혼용)", "조세호", "선미"],
        "comment": "이불 속이 제일 안전해요. 오늘 밤도 300가지 상상하다 새벽 4시에 잠들 예정! 🛌💭",
    },
    "INTP": {
        "title": "🧪 걸어다니는 위키백과 & 방구석 천재",
        "celebs": ["BTS 진", "정은지", "기안84", "휘인"],
        "comment": "'그게 왜 그렇지?' 생각하다 밤새우는 당신. 남들이 보기엔 멍때리는 것 같지만 뇌는 풀가동 중! 🧬",
    },
    "EFPT": {  # 만약의 오타 방지용 기본 세팅 (아래 셀렉트박스로 정제)
        "title": "열정왕",
        "celebs": ["유재석"],
        "comment": "최고!",
    },
    "ENFJ": {
        "title": "👑 모두를 품는 오지랖 만렙 리더",
        "celebs": ["유재석", "BTS 지민", "임시완", "잭슨"],
        "comment": "남의 슬픔에 대신 울어주고 계신가요? 당신의 오지랖은 세상을 구합니다! 🦸‍♀️",
    },
    "ENTJ": {
        "title": "💼 걸어다니는 야망 야망 야망덩어리",
        "celebs": ["이승기", "유노윤호", "스윙스", "티파니"],
        "comment": "오늘도 열정 폭발! '오늘 할 일을 내일로 미루지 마라, 내일 할 것도 오늘 해라!' 🔥",
    },
    "ESFP": {
        "title": "🕺 침묵을 못 견디는 인간 무지개",
        "celebs": ["비(Rain)", "수영(소녀시대)", "주호민", "하성운"],
        "comment": "어딜 가나 조명이 당신을 조명하네~ 조용하면 몸이 쑤시는 슈퍼 스타! 🌈",
    },
    "ESTP": {
        "title": "🏎️ 스릴을 즐기는 본투비 인싸",
        "celebs": ["전현무", "태현(TXT)", "경리", "손담비"],
        "comment": "고민은 배송만 늦출 뿐! 일단 지르고 보는 당당한 본투비 액션파 😎",
    },
    "ISFP": {
        "title": "🛋️ 누워있는 게 제일 좋아, 예술가",
        "celebs": ["BTS 정국", "유재석(혼용)", "백현", "슬기(레드벨벳)"],
        "comment": "눕기의 달인! '내일 하자...'라고 말하며 세상에서 가장 편안한 자세를 찾는 중 💤",
    },
    "ISTP": {
        "title": "🛠️ 만능 손재주꾼 & 마이웨이 끝판왕",
        "celebs": ["박명수", "BTS 슈가(혼용)", "안유진(IVE)", "홍진경"],
        "comment": "귀찮은 건 딱 질색! 효율 극대화를 노리는 냉철하지만 속정 깊은 사람 🔧",
    },
    "ESFJ": {
        "title": "🍰 핵인싸 친절왕 & 분위기 메이커",
        "celebs": ["BTS 제이홉", "광희", "혜리", "박보검"],
        "comment": "모두가 행복해야 마음이 편안해지는 인싸 중의 인싸! 리액션 부자 👏",
    },
    "ESTJ": {
        "title": "📐 단호박 현실주의자 & 엄격한 관리자",
        "celebs": ["한가인", "데프콘", "김구라", "이지혜"],
        "comment": "비효율적인 꼴은 절대 못 봄! 당신의 말 한마디면 프로젝트 깔끔 정리 📋",
    },
    "ISFJ": {
        "title": "🛡️ 세상 제일 다정한 헌신적인 수호자",
        "celebs": ["태용(NCT)", "다현(트와이스)", "안영미", "영탁"],
        "comment": "남 챙기느라 정작 자신은 못 챙기는 천사... 오늘만큼은 본인을 챙겨주세요 👼",
    },
    "ISTJ": {
        "title": "📏 FM의 정석! 인간 정밀 저울",
        "celebs": ["차은우", "써니(소녀시대)", "성규(인피니트)", "이석훈"],
        "comment": "규칙은 지키라고 있는 것! 계획표대로 살아갈 때 가장 마음이 편안해지는 인간 엑셀 📊",
    },
}

mbti_list = sorted(list(mbti_db.keys()))

# 사용자 입력 받기
selected_mbti = st.selectbox(
    "👉 당신의 MBTI를 선택해 주세요!", mbti_list, index=0
)

st.write("")  # 간격 조절

if st.button("🔮 소울메이트 연예인 확인하기!", use_container_width=True):
    # 효과음 및 연출
    st.balloons()

    info = mbti_db[selected_mbti]

    # 결과 출력 카드
    st.markdown(
        f"""
        <div class="mbti-box">
            <h2>[{selected_mbti}] {info['title']}</h2>
            <p style="font-size: 1.1rem; color: #333;">{info['comment']}</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.subheader(f"✨ {selected_mbti} 대표 연예인 라인업!")

    # 연예인 목록을 가로 컬럼 형태로 이쁘게 나열
    cols = st.columns(len(info["celebs"]))
    for idx, celeb in enumerate(info["celebs"]):
        with cols[idx % len(cols)]:
            st.info(f"👤 **{celeb}**")

    # 코믹한 행운의 메시지
    st.divider()
    random_luck = random.choice(
        [
            "오늘 길가다 500원을 줍게 될 확률 99%!",
            "오늘 밤 맛있는 야식을 먹어도 살이 안 찔 운세!",
            "당신의 MBTI 매력 지수가 상승했습니다 (+100)",
            "최애 연예인과 꿈에서 만날 확률 급상승!",
        ]
    )
    st.success(f"🍀 **오늘의 럭키 포춘:** {random_luck}")
