from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),

]
