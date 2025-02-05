from rest_framework.views import APIView
from rest_framework.response import Response
from .bots import translate_bot

class TranslateAPIView(APIView):
    
    def post(self, request):
        data = request.data # request 받은 data를 data에 넣기
        message = data.get("message", "") # message는 data에 있는 "message" 값 들고 오기
        translated_message = translate_bot(message) # 번역할 메시지는 translate_bot에 있는 message 로직으로 하기
        return Response({"translated_message": translated_message})
        