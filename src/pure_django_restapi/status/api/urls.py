from django.conf.urls import url, include
from .views import (
    StatusAPIView,StatusAPIDetailView,
    # StatusCreateAPIView,
    # StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView
    )


urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view()),
    # url(r'^create/$', StatusCreateAPIView.as_view()), Not needed now after using mixin as StatusAPIView is handling it already
    
    # url(r'^(?P<pk>.*)/$', StatusDetailAPIView.as_view()),-> for passing pk directly, otherwise you'll have to pass id as kwargs
    # url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),
]

# Start with
# api/status - list
# api/status/create - Create view
# api/status/12 - Detail
# api/status/12/update/ - Update
# api/status/12/delete/ - Delete

# End with

# /api/status/ -> List -> CRUD
# /api/status/1/ -> Detail -> CRUD

# Finally,

# /api/status/ -> CRUD & List&Search
