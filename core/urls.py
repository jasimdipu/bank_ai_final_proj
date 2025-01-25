from django.contrib import admin
from django.urls import path, include
#
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions
#
# # Swagger setup
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Final Project",
#         default_version='v1',  # Add the default version here
#         description="This documentation is intended to simplify the API implementation.",
#         terms_of_service="",
#         contact=openapi.Contact(email="dipu.j247@gmail.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('customers/', include('model_train.urls')),  # Fixed typo from 'cutomers' to 'customers'
    path('test-module/', include('test.urls')),  # Fixed typo from 'cutomers' to 'customers'
]
