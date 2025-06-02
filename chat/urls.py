from django.urls import path

from chat.views import ChatProductAPIView

urlpatterns = [
    path('chat/', ChatProductAPIView.as_view(), name='chat-api'),
]
