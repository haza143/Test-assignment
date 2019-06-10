from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from . import views
from django.urls import path, include
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .viewsets import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    url(r'^', include('rest_auth.urls')),
    url(r'^', include(router.urls)),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

# from django.conf.urls import url, i   nclude
# from rest_framework import routers
# from api.views import UserViewSet
#
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
#
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^auth/', include('rest_auth.urls')),
# ]
