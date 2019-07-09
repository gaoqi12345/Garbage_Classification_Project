from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^login',views.login_view,name='login'),
    url(r'^register',views.register_view,name='register'),
    url(r'^forget_password',views.forget_password_view,name='forget_password'),
    url(r'^user_info',views.user_info_view,name='user_info'),
]