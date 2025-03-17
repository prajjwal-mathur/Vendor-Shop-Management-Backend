from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, ShopListCreateView, ShopDetailView, NearbyShopsView, TokenPairGenerationView
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', RegisterView.as_view(), name='Vendor Registration'),
    path('login/', TokenPairGenerationView.as_view(), name='Login Page'),
    path('login/refresh/', TokenRefreshView.as_view(), name='Login Refresh'),
    path('shops/', ShopListCreateView.as_view(), name='Create/List Shops'),
    path('shops/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
    path('shops/nearby/', NearbyShopsView.as_view(), name='nearby-shops'),
]
