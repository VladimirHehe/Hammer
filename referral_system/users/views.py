import random
import string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render


class LoginView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        request.session['phone_number'] = phone_number
        verification_code = ''.join(random.choices(string.digits, k=4))
        request.session['verification_code'] = verification_code
        print(f"Verification code for {phone_number}: {verification_code}")
        return Response({"message": "Verification code sent."}, status=status.HTTP_200_OK)

    def get(self, request):
        return render(request, 'users/login.html')


class VerifyView(APIView):
    def post(self, request):
        phone_number = request.session.get('phone_number')
        code = request.data.get('code')

        if code == request.session.get('verification_code'):
            user, created = User.objects.get_or_create(phone_number=phone_number)
            return Response({"user_id": user.id}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid verification code!"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        phone_number = request.session.get('phone_number')
        return render(request, 'users/verify.html', {'phone_number': phone_number})


class ProfileView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return render(request, 'users/profile.html', {'user': serializer.data})

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        invite_code = request.data.get('invite_code')

        if user.activated_invite_code:
            return Response({"error": "Invite code already activated!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            invite_user = User.objects.get(invite_code=invite_code)
            user.activated_invite_code = invite_code
            invite_user.referred_users.add(user)
            user.save()
            invite_user.save()
            return Response({"success": "Invite code activated successfully!"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Invite code does not exist!"}, status=status.HTTP_404_NOT_FOUND)


class ActivateInviteView(APIView):
    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        invite_code = request.data.get('invite_code')

        if user.activated_invite_code:
            return Response({"error": "Invite code already activated!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            invite_user = User.objects.get(invite_code=invite_code)
            user.activated_invite_code = invite_code
            invite_user.referred_users.add(user)
            user.save()
            invite_user.save()
            return Response({"success": "Invite code activated successfully!"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Invite code does not exist!"}, status=status.HTTP_404_NOT_FOUND)