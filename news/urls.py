"""
URL configuration for NewsPortal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# Импортируем созданное нами представление
from .views import (PostList, NewDetail, PostCreate, PostUpdate, PostDelete, PostSearch)



urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', NewDetail.as_view(), name='new_detail'),
    path('search/', PostSearch.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
]