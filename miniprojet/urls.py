
from django.contrib import admin
from django.urls import include, path
from portfolio import views
urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('portfolio/', include('portfolio.urls')),
    path('formation/',include('formation.urls'))
    
    
]
