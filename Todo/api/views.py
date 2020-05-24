from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import  generics
from .models import TodoModel
from .serializers import TodoSerializer


@api_view(['GET', "POST"])
def TodoIndex(request):
    if request.method == 'GET':
        data = TodoModel.objects.all()
        serializer = TodoSerializer(data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class RUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'


