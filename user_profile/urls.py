from django.conf.urls import url
from user_profile.views import PersonCreateView, PersonListView, PersonUpdateView


app_name = 'user_profile'
urlpatterns = [
    url(r'^$', PersonListView.as_view(), name='index'),
    url(r'^user_profile/$', PersonCreateView.as_view(), name='user-profile-create'),
    url(r'^/$', PersonUpdateView.as_view(), name='user-profile-update')
]
