from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from web import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('web.urls',namespace='web')),
    # path('blog',include('blog.urls',namespace='blog')),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    
       
    
admin.site.site_header = "PROJECT Administration"
admin.site.site_title = "PROJECT Admin Portal"
admin.site.index_title = "Welcome to PROJECT Admin Portal"
admin.site.index_title = "Welcome to PROJECT Admin Portal"
