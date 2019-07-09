from django.conf.urls import url

from forum import views
urlpatterns = [
    url(r'^index$',views.forum_index_view,name='forum_index'),
    url(r'^special_topic$',views.special_topic_view,name='special_topic'),
]