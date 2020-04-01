import json
from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializer

def is_json(data):
    try:
        real_json = json.loads(data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid
#CreateModelMixin -> POST method
#UpdateModelMixin -> PUT method
#DestroyModelMixin -> DELETE method

class StatusAPIDetailView(
    generics.RetrieveAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin):
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes  = []
    serializer_class        = StatusSerializer
    queryset                = Status.objects.all
    lookup_field            = 'id'
    # passed_id               = None

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     serializer.save(updated_by_user = self.request.user)

    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id') #Same as that specified in the urls.py
        return Status.objects.get(id=kw_id)


class StatusAPIView(mixins.CreateModelMixin,
    # mixins.RetrieveModelMixin,
    generics.ListAPIView):
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes  = [SessionAuthentication]
    serializer_class        = StatusSerializer
    passed_id               = None

    def get_queryset(self):
        request = self.request
        # print(request.user)
        qs = Status.objects.all()
        print("Call came to get_queryset")
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    # def get_object(self):
    #     request     = self.request
    #     passed_id   = request.GET.get('id', None) or self.passed_id
    #     queryset    = self.get_queryset()
    #     obj = None
    #     if passed_id is not None:
    #         obj = get_object_or_404(queryset, id=passed_id)
    #         self.check_object_permissions(request, obj)
    #     return obj

    # def get(self, request, *args, **kwargs):
    #     url_passed_id   = request.GET.get('id', None)
    #     json_data       = {}
    #     body_           = request.body
    #     if is_json(body_):
    #         json_data   = json.loads(request.body)
    #     new_passed_id   = json_data.get('id', None)

    #     passed_id = url_passed_id or new_passed_id or None
    #     self.passed_id = passed_id
    #     if passed_id is not None:
    #         return self.retrieve(request, *args, **kwargs)
    #     return super().get(request, *args, **kwargs)

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


