from django.urls import path
from open_ai.api.views import PostMessage

urlpatterns = [
    path('chat', PostMessage.as_view())
]
