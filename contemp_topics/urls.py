from django.urls import include
from django.conf.urls import url
from contemp_topics.views import HomePageView, get_polygons, EditForm

urlpatterns = [
    url(r'^$',HomePageView.as_view(), name = 'home'),
    url(r'^polygons$',get_polygons, name='polygon'),
]
