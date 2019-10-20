import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# from django.core.serializers import serialize

from .models import Update


from pure_django_restapi.mixins import JsonResponseMixin

from django.views.generic import View
# Create your views here.
def json_example_view(request):
    '''
    URI - for a REST api
    Get - Retrieve data
    '''
    data = {
        "count" : 1000,
        "content" : "Some new content"
    }
    return JsonResponse(data)

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count" : 1000,
            "content" : " Some New Content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count" : 1000,
            "content" : " Some New Content"
        }
        return self.render_to_json_response(data)

class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=2)
        # json_data = serialize("json" , [obj,], fields = ('user','content'))
        json_data = obj.serialize()

        return HttpResponse(json_data, content_type='application/json')

class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        # data = serialize("json" , qs, fields = ('user','content'))

        json_data = Update.objects.all().serialize()
        # data = {
        #     "user" : obj.user.username,
        #     "content" : obj.content
        # }
        # json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
