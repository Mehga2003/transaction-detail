from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from notes import views


urlpatterns = [

    # =========================
    # PROMETHEUS METRICS
    # =========================
    path(
        '',
        include('django_prometheus.urls')
    ),

    # =========================
    # ADMIN
    # =========================
    path(
        'admin/',
        admin.site.urls
    ),

    # =========================
    # NOTES APP ROUTES
    # =========================
    path(
        '',
        include('notes.urls')
    ),

    # =========================
    # TRANSACTION API
    # =========================

    # GET + POST
    path(
        'api/transactions/',
        views.transactions_api,
        name='transactions_api'
    ),

    # UPDATE + DELETE
    path(
        'api/transactions/<int:id>/',
        views.transaction_detail,
        name='transaction_detail'
    ),

    # =========================
    # AUTH
    # =========================
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # =========================
    # JWT TOKEN
    # =========================
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]