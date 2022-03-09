from rest_framework.response import Response
from rest_framework.decorators import api_view
from UserApp.models import User
from .serializers import UserSerializer


@api_view(['GET'])  # This is a decorator
def getData(request):
    userArray = User.objects.all()
    serializer = UserSerializer(userArray, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)