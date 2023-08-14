from django.contrib import admin
from table.models import (
    Restaurant,
    Table,
    Plate,
)

# Register your models here.
admin.site.register([Restaurant, Table, Plate])
