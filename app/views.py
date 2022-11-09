from rest_framework.generics import ListAPIView, RetrieveAPIView

from app.models import Todo
from app.serializers import TodoSerializer


# Create your views here.

class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
