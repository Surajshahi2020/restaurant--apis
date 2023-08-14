from django.urls import path, include
from rest_framework.routers import DefaultRouter

from table.api.viewsets.table_occupied import TableViewSet

urlpatterns = [
    path("table-plate-create", TableViewSet.as_view()),
]
