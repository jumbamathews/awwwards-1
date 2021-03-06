from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index , name="home"),
    path('signup/',views.signup,name="signup"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('upload/',views.uploads,name="uploads"),
    path('search/',views.search,name='search'),
    path('site/<id>',views.site,name='site'),
    path('profile/<username>',views.profile,name='profile'),
    path('settings/',views.settings,name='settings')
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
