"""CollegeMania URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('', ListItem.as_view()),
    path('item', ListItem.as_view()),
    path('item/<int:pk>/', DetailsItem.as_view()),
    path('Campus', ListCampus.as_view()),
    path('Campus/<int:pk>/', DetailsCampus.as_view()),
    path('ItemCategory', ListItemCategory.as_view()),
    path('ItemCategory/<int:pk>/', DetailsItemCategory.as_view()),
    path('ItemImage', ListItemImage.as_view()),
    path('ItemImage/<int:pk>/', DetailsItemImage.as_view()),
    path('Conversation', ListConversation.as_view()),
    path('Conversation/<int:pk>/', DetailsConversation.as_view()),
    path('Message', ListMessage.as_view()),
    path('Message/<int:pk>/', DetailsMessage.as_view()),
    path('User', ListUser.as_view()),
]
