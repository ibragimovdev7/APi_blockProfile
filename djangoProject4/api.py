from rest_framework import routers
from app1 import views

router = routers.DefaultRouter()
router.register(r'profile',views.ProfileView,basename='profile')