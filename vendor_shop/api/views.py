from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from geopy.distance import geodesic
from .models import Shop
from .serializers import ShopSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response


class RegisterView(APIView):
    def post(self, request):
        full_name = request.data['full_name']
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password or not full_name:
            return Response({"error": "Username, full name and password required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "User already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "Vendor registered successfully!"}, status=status.HTTP_201_CREATED)


class TokenPairGenerationView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data['redirect_url'] = '/shops/'
        return response


class ShopListCreateView(generics.ListCreateAPIView):
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Shop.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class NearbyShopsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        lat = float(request.GET.get('lat'))
        lon = float(request.GET.get('lon'))
        radius_km = float(request.GET.get('radius', 5))

        shops = Shop.objects.all()
        nearby_shops = [
            shop for shop in shops
            if geodesic((lat, lon), (shop.latitude, shop.longitude)).km <= radius_km
        ]

        serializer = ShopSerializer(nearby_shops, many=True)
        return Response(serializer.data)
