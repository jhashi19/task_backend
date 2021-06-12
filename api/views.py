from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Task
from .serializers import (
    MyTokenObtainPairSerializer,
    TaskSerializer,
    UserSerializer
)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# 以下、ModelViewSetで置き換える？
class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    # Taskモデルのdrafterにログインユーザが設定されるようにオーバーライドする記述を追加する。

    def perform_create(self, serializer):
        try:
            serializer.save(drafter=self.request.user)
        except BaseException:
            raise ValueError('fail to save drafter.')


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
