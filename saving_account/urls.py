from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SavingTypeList, SavingTypeDetail, SavingAccountList,SavingAccountDetail,SavingList,SavingDetail


urlpatterns = [
    #Saving Type
    path('savingtype/',SavingTypeList.as_view()),
    path('savingtype/<str:slug>/',SavingTypeDetail.as_view()),

    #Saving Account
    path('savingaccount/',SavingAccountList.as_view()),
    path('savingaccount/<str:pk>/',SavingAccountDetail.as_view()),

    #Saving
    path('saving/',SavingList.as_view()),
    path('saving/<str:pk>/',SavingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
