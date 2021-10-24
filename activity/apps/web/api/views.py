from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from .serializers import *
from .filters import *
from ..models import *


class AddActivityViewSet(viewsets.ModelViewSet):
    """
    API para registrar actividades
    """
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all().order_by('-created_at_datetime')
    filterset_fields = ['ic', 'title']

    def list(self, request):
        kwargs = {}
        if 'schedule_start' in self.request.query_params:
            kwargs['schedule__date__gte'] = self.request.query_params['schedule_start']
        if 'schedule_end' in self.request.query_params:
            kwargs['schedule__date__lte'] = self.request.query_params['schedule_end']
        if 'status' in self.request.query_params:
            kwargs['status'] = self.request.query_params['status']

        queryset = Activity.objects.filter(**kwargs)
        serializer = ActivitySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            try:
                property_obj = serializer.validated_data['property']
                if property_obj.status != "ACT":
                    return Response({'property': 'La propiedad debe tener el estatus activada'}, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response({'message': 'Actividad creada'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


