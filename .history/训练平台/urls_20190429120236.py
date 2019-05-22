from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('tools/', include('tools.urls')),
    # path('admin/', admin.site.urls),
    path('', include('sql.urls')),
]
