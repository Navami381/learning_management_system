from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.models import User,StudentProfile,TrainerProfile
from accounts.serializers import UserSerializer,StudentSerializer,TrainerProfileSerializer
from accounts.permissions import IsAdminUser

# Create your views here.
class AdminCreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            instance=User.objects.create_superuser(role="trainer",**cleaned_data)
            serializer_instance=UserSerializer(instance)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class StudentCreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            instance=User.objects.create_user(**cleaned_data)
            serializer_instance=UserSerializer(instance)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class TrainerProfileUpdateView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def put(self,request):

        form_data=request.data

        trainer_obj=TrainerProfile.objects.get(trainer=request.user)

        serializer_instance=TrainerProfileSerializer(data=form_data,instance=trainer_obj)

        if serializer_instance.is_valid(): 

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

    

class TrainerProfileMeView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def get(self,request):

        qs=TrainerProfile.objects.get(trainer=request.user)

        serializer_instance=TrainerProfileSerializer(qs)

        return Response(data=serializer_instance.data)