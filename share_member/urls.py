from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ShareMemberList,ShareMemberDetail


urlpatterns = [
    path('sharemembers/',ShareMemberList.as_view()),
    path('sharemembers/<str:pk>/',ShareMemberDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
