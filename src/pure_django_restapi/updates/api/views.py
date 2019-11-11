from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel
import json

from .mixins import CSRFExempMixin
from pure_django_restapi.mixins import HttpResponseMixin

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExempMixin, View):
    '''
    Retrieve, Update, Delete --> Object
     '''
    is_json = True
    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        print("Object is : ",obj.content)
        json_data = obj.serialize()
        return self.render_to_response(json_data)
        #json could also be xml, yaml

    def post(self, request, *args, **kwargs):
        data = {}
        return self.render_to_response(data, status = 400)

    def put(self, request, *args, **kwargs):
        data = {}
        return self.render_to_response(data)

    def delete(self, request, *args, **kwargs):
        data = {}
        return self.render_to_response(data, status = 403)

class UpdateModelListAPIView(HttpResponseMixin, CSRFExempMixin, View):
    '''
        We usually have only get in detail view, ofcourse we can also have all
        of these as well, it really depends on the use case.
        For now, we will only use get in the detail view.
        Also, sometimes you'll see that the individual methods are broken out
        in different classes.

    '''
    is_json = True
    # def render_to_response(data, status=200):
    #     return HttpResponse(data, content_type = 'application/json',
    #                         status = status)

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        data = json.dumps({"message":"Unknown data"})
        # return HttpResponse(data, content_type = 'application/json', status = 400)
        return self.render_to_response(data, status = 400)
    '''

    def put(self, request, *args, **kwargs):

        return #json could also be xml, yaml
        '''

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message":"You cannot delete an entire list"})
        # status_code = 403 #Forbidden
        return self.render_to_response(data, status = 403)
