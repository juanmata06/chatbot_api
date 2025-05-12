from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from open_ai.api.serializers import PostMessageSerializer
from open_ai.models import Chat

from openai import OpenAI
client = OpenAI(api_key="")


class PostMessage(APIView):
    def post(self, request):
        serializer = PostMessageSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = client.responses.create(
                model="gpt-4.1",
                input=serializer.validated_data['prompt']
            )

            # chat = Chat.objects.create(
            #     user=user,
            #     message=prompt,
            #     response=response.output_text
            # )

            return Response({"response": response.output_text}, status=status.HTTP_201_CREATED)
        
        except client.OpenAIError as e:
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)
