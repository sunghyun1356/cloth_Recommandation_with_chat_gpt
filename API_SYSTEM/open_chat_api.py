import openai
from API_SYSTEM.weather_finding import show
# 발급 받는 API 키 설정
def api_answer(a):
        OPENAI_API_KEY = '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'

        #OPEN API 키 인증

        openai.api.key  = OPENAI_API_KEY

        #대답 불러오기
        

        # 모델 - GPT 3.5 Turbo 선택
        model = "gpt-3.5-turbo"

        # 질문 작성하기
        query = f'{a}'

        # 메시지 설정하기
        messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
        ]

        # ChatGPT API 호출하기
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages
        )
        answer = response['choices'][0]['message']['content']
        returnanswer
