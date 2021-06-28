from shortner.views import redirect_shortner, UrlViewSet
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url

#from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

#schema_view = get_swagger_view(title='Shortme API')
schema_view = get_schema_view(title='Shortme API', renderer_classes=[
                              OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    path('', schema_view, name="docs"),
    path('admin/', admin.site.urls),
    path('api/v1/csu/', UrlViewSet.as_view()),
    path('<str:slug>/', redirect_shortner),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
