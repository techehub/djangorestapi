from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/puppies/(?P<pk>[0-9]+)$',
        views.PuppyDetail.as_view(),

    ),
    url(
        r'^api/puppies/$',
        views.PuppyList.as_view(),

    )
]