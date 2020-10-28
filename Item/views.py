from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializer import *
from .models import *
from django.http import Http404
# from .models import Profile
from rest_framework.authtoken.models import Token

from rest_framework import decorators
from rest_framework import parsers
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import I
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, BasePermission

# from rest_framework.permissions import T

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class CustomUserPermissionOfUserPostPatchPut(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS and request.POST.get('user_id') and request.POST.get('user_id') != str(
                request.user.id):
            return False
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data
        })


class ListUser(generics.ListCreateAPIView):
    # permission_classes = (CustomUserPermissionOfUserPostPatchPut,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListItem(generics.ListCreateAPIView):
    permission_classes = (CustomUserPermissionOfUserPostPatchPut,)
    queryset = Item.objects.filter(status_sold=False)
    serializer_class = ItemSerializer


class DetailsItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomUserPermissionOfUserPostPatchPut,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ListItemCategory(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer


class DetailsItemCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategoryWithItemSerializer


class ListCampus(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class DetailsCampus(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class ListItemImage(generics.ListCreateAPIView):
    permission_classes = (CustomUserPermissionOfUserPostPatchPut,)
    queryset = ItemImage.objects.all()
    serializer_class = ItemImageSerializer


class DetailsItemImage(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomUserPermissionOfUserPostPatchPut,)
    queryset = ItemImage.objects.all()
    serializer_class = ItemImageSerializer


class ListConversation(generics.ListCreateAPIView):
    permission_classes = (CustomUserPermissionOfUserPostPatchPut,)
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class DetailsConversation(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomUserPermissionOfUserPostPatchPut,)
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class ListMessage(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class DetailsMessage(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# class ListUser(generics.ListCreateAPIView):
#     permission_classes = (CustomUserPermissionOfUserPostPatchPut,)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
