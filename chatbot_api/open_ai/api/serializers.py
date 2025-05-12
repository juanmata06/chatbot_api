from rest_framework import serializers
from open_ai.models import Prompt


class PostMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['prompt']
