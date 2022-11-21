# main urls

from django.contrib import admin
from django.urls import path, include

from main import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
