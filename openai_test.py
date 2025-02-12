from openai import OpenAI
from api_pjt import config

CLIENT = OpenAI(api_key=config.OPENAI_API_KEY)

def ask_to_gpt(instructions, message):
    completion = CLIENT.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": instructions,
            },
            {
                "role": "user",
                "content": message,
            },],)
    return completion.choices[0].message.content

# 프롬포트
system_instructions = """
이제부터 너는 '민경 카페'의 직원이야.
아래 종류의 음료 카테고리에서 주문을 받고, 주문을 처리하는 대화를 진행해.

1. 초코라떼
2. 고구마라떼
3. 밤라떼
4. 뱅쇼
5. 딸기주스

주문을 받으면, 주문 내용을 확인하고, 주문을 처리하는 대화를 진행해.
주문이 완료되면, 주문 내용을 확인하고, 주문이 완료되었음을 알려줘.
"""

# 처음 인사를 위해
response = ask_to_gpt(system_instructions, "")
print(f"민경 카페봇 : {response}\n\n")

while True:
    user_message = input("유저 : ")
    if user_message == "종료":
        break
    response = ask_to_gpt(system_instructions, user_message)
    print(f"민경 카페봇 : {response}\n\n")
