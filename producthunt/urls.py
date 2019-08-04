
from django.contrib import admin
from django.urls import path,include
import products.views
import accounts

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', products.views.home, name='home'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('products/', include('products.urls'), name='products'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
