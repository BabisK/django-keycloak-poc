from django.urls import include, path

from app.views import ProfileView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', ProfileView.as_view())
]