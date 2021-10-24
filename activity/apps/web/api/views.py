from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from .serializers import *
from ..models import *
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
import datetime


class AddActivityViewSet(viewsets.ModelViewSet):
    """
    API para registrar actividades
    """
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all().order_by('-created_at_datetime')

    def list(self, request):
        kwargs = {}
        if self.request.query_params == {}:
            kwargs['schedule__date__gte'] = (datetime.datetime.now() - datetime.timedelta(days=3)).date()
            kwargs['schedule__date__lte'] = (datetime.datetime.now() + datetime.timedelta(days=14)).date()
        else:
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

    @action(detail=False, methods=['post'])
    def cancel_activity(self, request):
        serializer = ActivityCancelSerializer(data=request.data)
        if serializer.is_valid():
            try:
                activity = get_object_or_404(Activity, id=serializer.validated_data['id'])
                activity.status = serializer.validated_data['status']
                activity.save()
                return Response({'message': 'Actividad cancelada'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def change_status_activity(self, request):
        serializer = ActivityChangeStatusSerializer(data=request.data)
        if serializer.is_valid():
            try:
                activity = get_object_or_404(Activity, id=serializer.validated_data['id'])
                activity.status = serializer.validated_data['status']
                activity.save()
                return Response({'message': 'Estatus actualizado'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def reschedule_activity(self, request):
        serializer = ActivityRescheduleSerializer(data=request.data)
        if serializer.is_valid():
            try:
                activity = get_object_or_404(Activity, id=serializer.validated_data['id'])
                if activity.status == "DES":
                    return Response({'property': 'No se puede reagendar una actividad cancelada'}, status=status.HTTP_400_BAD_REQUEST)
                activity.schedule = serializer.validated_data['schedule']
                activity.updated_at_datetime = datetime.datetime.now()
                activity.save()
                return Response({'message': 'Actividad reagendada'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



