from django.contrib import admin
from django.urls import path, include

from works.views import AppealView
from works.views import ProjectViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('appeals/', AppealView.as_view(), name='appeals'),
    path('works/', include('works.urls')),
]
