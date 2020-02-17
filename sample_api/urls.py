from django.conf.urls import url, include
from django.contrib import admin

from users_manage.url import router as users_manage_router

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    # blog.urlsをincludeする
    #url(r'^api/', include(router.urls)),
    url(r'^api/', include(users_manage_router.urls)),
]
