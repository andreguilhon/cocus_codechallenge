from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'readers', views.FileContentViewSet)

urlpatterns = [
    path('reader/', views.FileContentViews.as_view()),
    path('reader/<int:line_number>', views.FileContentViews.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]