from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.demo),
    path('login/', views.login_user),
    path('register', views.register_user),
    path('logout-user', views.logout_user),
    path('user-profile/<int:pk>', views.user_profile),
    path('search-product', views.search_product),
    path('api-test', views.api_test),
    path('abc', views.ProductsApi.as_view()),
    path('xyz', views.Demo.as_view()),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
