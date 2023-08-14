from rest_framework import generics
from rest_framework.response import Response
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiResponse,
    OpenApiExample,
)

from table.api.serializers.table_occuped import TableSerializer
from table.models import Table, Plate


@extend_schema_view(
    post=extend_schema(
        summary="Refer to Schema At Bottom",
        examples=[
            OpenApiExample(
                name="Single Table",
                request_only=True,
                value={
                    "table_data": {
                        "table1": {
                            "position_x": 1.2,
                            "position_y": 1.3,
                            "name": "table1",
                            "restaurant": 1,
                            "plates": [
                                {"position_x": 1.2, "position_y": 1.3},
                                {"position_x": 1.2, "position_y": 1.3},
                            ],
                        }
                    },
                },
            ),
            OpenApiExample(
                name="Multiple Table",
                request_only=True,
                value={
                    "table_data": {
                        "table1": {
                            "position_x": 1.2,
                            "position_y": 1.3,
                            "name": "table1",
                            "restaurant": 1,
                            "plates": [
                                {"position_x": 1.2, "position_y": 1.3},
                                {"position_x": 1.2, "position_y": 1.3},
                            ],
                        },
                        "table2": {
                            "position_x": 1.2,
                            "position_y": 1.3,
                            "name": "table2",
                            "restaurant": 1,
                            "plates": [
                                {"position_x": 1.2, "position_y": 1.3},
                                {"position_x": 1.2, "position_y": 1.3},
                            ],
                        },
                    },
                },
            ),
        ],
        description="Login Api",
        request=TableSerializer,
        responses={
            200: OpenApiResponse(
                description="Success Response when user is registered successfully",
            ),
            422: OpenApiResponse(
                description="Json Data Error, occurs when invalid data is sent!",
            ),
        },
        tags=["Table and Plate Apis"],
    ),
)
class TableViewSet(generics.CreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                "title": "Table",
                "message": "Table and Plates created successfully",
                "data": response.data,
            }
        )
