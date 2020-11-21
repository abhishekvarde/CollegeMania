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
    path('', ListItem.as_view()),
    path('item', ListItem.as_view()),
    path('item/<int:pk>/', DetailsItem.as_view()),
    path('campus', ListCampus.as_view()),
    path('campus/<int:pk>/', DetailsCampus.as_view()),
    path('item_category', ListItemCategory.as_view()),
    path('item_category/<int:pk>/', DetailsItemCategory.as_view()),
    path('item_image', ListItemImage.as_view()),
    path('item_image/<int:pk>/', DetailsItemImage.as_view()),
    path('conversation', ListConversation.as_view()),
    path('conversation/<int:pk>/', DetailsConversation.as_view()),
    path('message', ListMessage.as_view()),
    path('message/<int:pk>/', DetailsMessage.as_view()),
    path('item_by_campus_id/<int:pk>/', DetailsItemWithCampusId.as_view()),
    path('my_items/<int:pk>/', DetailsMyItems.as_view()),
]
