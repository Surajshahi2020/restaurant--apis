from rest_framework import serializers

from table.models import (
    Table,
    Restaurant,
    Plate,
)

from common.exceptions import UnprocessableEntityException


class TableSerializer(serializers.Serializer):
    table_data = serializers.JSONField()

    def to_representation(self, instance):
        return self.validated_data.get("table_data")

    def create(self, validated_data):
        tables = []
        data = validated_data.get("table_data").items()
        for table_tuple in data:
            table_name, table_value = table_tuple
            table_data = {
                "name": table_value.get("name", None),
                "position_x": table_value.get("position_x", None),
                "position_y": table_value.get("position_y", None),
                "restaurant": table_value.get("restaurant", None),
            }
            restaurant_id = table_data.get("restaurant")
            if restaurant_id is not None:
                restaurant = Restaurant.objects.get(id=restaurant_id)
                table_data["restaurant"] = restaurant

            table = Table.objects.create(
                name=table_data.get("name"),
                position_x=table_data.get("position_x"),
                position_y=table_data.get("position_y"),
                restaurant=table_data.get("restaurant"),
            )

            plates_data = table_value.get("plates", [])
            plates = []
            for plate_data in plates_data:
                if not len(plates_data) > 4:
                    plate = Plate.objects.create(
                        position_x=plate_data.get("position_x"),
                        position_y=plate_data.get("position_y"),
                        restaurant=restaurant,
                        table=Table.objects.get(id=table.id),
                    )
                    plates.append(plate)
                else:
                    raise UnprocessableEntityException(
                        {
                            "title": "T  able",
                            "message": "Number of plates must not exceed 4",
                        }
                    )

            table.plates.set(plates)
            tables.append(table)

        return tables
