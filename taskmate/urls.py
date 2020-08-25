from django.contrib import admin
from django.urls import path, include
# se importan las vistas de la app todolist_app y se crea un alias porque a futuro uno va a tener
# multiples apps y multiples vistas, entonces de esta forma se puede identificar univocamente  
from todolist_app import views as todolist_views
 
urlpatterns = [
    #path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    
    path('', todolist_views.index, name='index'),
    path('todolist/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('contact', todolist_views.contact, name='contact'),
    path('about', todolist_views.about, name='about')
]