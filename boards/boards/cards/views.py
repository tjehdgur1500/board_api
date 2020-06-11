from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Card
from .serializer import CardSerializer, UserSerializer
from rest_framework import viewsets,permissions,status,generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.pagination import CursorPagination
from .permissions import IsOwnerOrReadOnly, IsOwner


class CursorPagination(CursorPagination):
    page_size = 2
    ordering = '-id'


class CardViewSet(viewsets.ModelViewSet):

    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    pagination_class = CursorPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class Logout(generics.DestroyAPIView):
    def delete(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

