from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator


class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="table", null=True, blank=True)
    position_x = models.FloatField()
    position_y = models.FloatField()
    type = models.CharField(max_length=1, default="T")
    is_occupied = models.BooleanField(default=False)
    plates = models.ManyToManyField("Plate", related_name="tables", blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def clean(self):
        if self.plates.count() > 4:
            raise ValidationError("A table cannot have more than 4 plates.")


class Plate(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, default="P")
    position_x = models.PositiveIntegerField()
    position_y = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.restaurant}---{self.table}"
