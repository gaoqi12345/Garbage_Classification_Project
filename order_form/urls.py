from django.conf.urls import url

from order_form import views

urlpatterns = [
    url(r'^index',views.order_index_view,name='order_form_index'),
    url(r'^message',views.message_view,name='message'),
]