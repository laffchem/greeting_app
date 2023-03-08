from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from oauth2_providers.decorators import protected_resource
from .models import Greeting
from .serializers import GreetingSerializer




@api_view(["GET", "POST"])
@protected_resource
def greeting(request):
    if request.method == "GET":
        messages = Greeting.objects.filter(active=True)
        serializer = GreetingSerializer(messages, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        if request.data == "hello":
            serializer = GreetingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({f"{serializer.data} : goodbye"}, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)