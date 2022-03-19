from rest_framework import routers
from django.urls import path, include
from . import views
from .views import ProductViewset, RemarkViewset


# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('product', ProductViewset, basename='product')
router.register('remark', RemarkViewset, basename='remark')

app_name = 'lefouineur'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls))
]
