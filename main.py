from quiz import Quiz

# 퀴즈 데이터
quizzes = [
    Quiz(
        "이탈리아 대표 음식으로, 둥글고 납작한 빵에 토핑을 얹어 구운 음식은?",
        "피자",
        ["1. 피자", "2. 파스타", "3. 리조또", "4. 라자냐"]
    ),
    Quiz(
        "일본 음식으로, 식초밥 위에 생선을 얹거나 김으로 싼 음식은?",
        "초밥",
        ["1. 라멘", "2. 우동", "3. 초밥", "4. 돈카츠"]
    ),
    Quiz(
        "밀가루 반죽을 얇게 밀어 다양한 모양으로 만든 이탈리아 음식은?",
        "파스타",
        ["1. 피자", "2. 파스타", "3. 뇨키", "4. 브루스케타"]
    ),
    Quiz(
        "고기나 채소를 빵 사이에 끼워 먹는 미국 대표 음식은?",
        "햄버거",
        ["1. 핫도그", "2. 샌드위치", "3. 햄버거", "4. 타코"]
    ),
    Quiz(
        "한국 대표 음식으로, 배추를 소금에 절여 양념에 버무린 발효 음식은?",
        "김치",
        ["1. 된장", "2. 고추장", "3. 간장", "4. 김치"]
    ),
]

def run_quiz():
    print("=== 🍽️ 음식 퀴즈 게임 ===\n")
    score = 0

    for i, quiz in enumerate(quizzes):
        print(f"Q{i+1}. {quiz.question}")
        for option in quiz.options:
            print(f"  {option}")
        
        user_answer = input("\n번호 또는 정답을 입력하세요: ").strip()

        if quiz.check_answer(user_answer):
            print("✅ 정답입니다!\n")
            score += 1
        else:
            print(f"❌ 오답입니다! 정답은 '{quiz.answer}' 입니다.\n")

    print(f"=== 최종 점수: {score} / {len(quizzes)} ===")

run_quiz()