from django.urls import path
from . import views

urlpatterns = [
    path('', views.loading_page, name='loading'),  # 로딩 화면
    path('main/', views.main_page, name='main'),  # 메인 페이지
]
