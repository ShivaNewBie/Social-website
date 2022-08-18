
from django.urls import path,include

from rest_framework.routers import DefaultRouter

from blog.api import views as bv

router = DefaultRouter()
router.register(r'blog', bv.BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]