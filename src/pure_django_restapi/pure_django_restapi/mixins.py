from django.http import JsonResponse, HttpResponse



class HttpResponseMixin(object):
    is_json = False
    def render_to_response(self, data, status=200):
        content_type = 'text/html'
        if self.is_json:
            content_type = 'application/json'

        return HttpResponse(data, content_type=content_type, status = status)

class JsonResponseMixin(object):

    def render_to_json_response(self, context, **kwargs):
        return JsonResponse(self.get_data(context), **kwargs)

    def get_data(self,context):
        return context
