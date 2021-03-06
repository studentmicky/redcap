from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views as rest_views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='RedCap API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tasks/', include('task_manager.task_urls')),
    url(r'^servers/', include('task_manager.servers_urls')),
    url(r'^projects/', include('task_manager.project_urls')),
    url(r'^manager/', include('task_manager.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', rest_views.obtain_auth_token),
    url(r'^$', schema_view)
]
