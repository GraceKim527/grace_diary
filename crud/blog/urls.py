from django.urls import path
from django.urls.resolvers import URLPattern
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.main, name = 'main'),
    path('write/', views.write, name = 'write'),
    path('write/create/', views.create, name = 'create'),
    path('edit/<str:id>', views.edit, name ='edit'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name ='delete'),
    path('comment/<str:id>', views.comment, name='comment'),
    path('hashtag/', views.hashtagform, name='hashtag'),
    path('<int:hashtag_id>/search/', views.search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)