from django.urls import path, include
from django_app import views
from rest_framework.routers import DefaultRouter

name_app = 'django_app'

router = DefaultRouter()
router.register('articles', views.ArticleViewSet, basename="articles")
router.register('generic-articles', views.ArticleGenericViewSet, basename="generic_articles_viewset")
router.register('model-articles', views.ArticleModelViewSet, basename="model_articles_viewset")

urlpatterns = [
    path('articles/', views.article_list, name="article_list"),
    path('articles/<int:pk>/', views.article_detail, name="article_detail"),
    path('views/articles', views.article_list_view, name="article_list_view"),
    path('views/articles/<int:pk>', views.article_detail_view, name="article_detail_view"),
    path('classes/articles/', views.ArticleList.as_view(), name="article_list_class"),
    path('classes/articles/<int:id>', views.ArticleDetail.as_view(), name="article_detail_class"),
    path('generics/articles/<int:id>/', views.GenericAPIView.as_view(), name="generic_articles"),
    path('authentication/articles/', views.AuthenticationAPIView.as_view(), name="authentication_articles"),
    path('viewsets/', include(router.urls)),
    path('viewsets/<int:id>', include(router.urls)),
]
