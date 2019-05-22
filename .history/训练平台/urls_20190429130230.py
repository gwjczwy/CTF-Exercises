from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('tools/', include('tools.urls')),
    path('', include('sql.urls')),
    # path('admin/', admin.site.urls),
]
