**myproject/myproject/urls.py**
python
from django.contrib import admin
from django.urls import path, include
from myapp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.admin_page, name='admin'),
    path('custom/', views.custom_page, name='custom'),
    path('admin/', admin.site.urls),
]
**myproject/myapp/views.py**
python
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
def home(request):
    return render(request, 'myapp/home.html')
@staff_member_required
def admin_page(request):
    return render(request, 'myapp/admin.html')
def custom_page(request):
    return render(request, 'myapp/custom.html')
shell
python manage.py runserve
#Приложение будет доступно по адресу http://localhost:8000/.
