from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',include('backend.core.urls', namespace='core')),
    path('servico/',include('backend.servico.urls', namespace='servico')),
    path('admin/', admin.site.urls),
]
