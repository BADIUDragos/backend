from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from base.test.models import TestModel
from base.test.serializers import TestModelSerializer


class TestModelListView(APIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer
    permission_classes = [DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        queryset = TestModel.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
