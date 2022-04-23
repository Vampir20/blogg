from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'Articles.views.view404'

urlpatterns = [
    path('', include('Main.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('News.urls')),
    path('articles/',include('Articles.urls')),
    path('reviews/', include('Reviews.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
