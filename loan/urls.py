from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    #Loan Type
    path('loantype/',LoanTypeList.as_view()),
    path('loantype/<str:slug>/',LoanTypeDetail.as_view()),

    #Loan Account
    path('loanaccount/',LoanAccountList.as_view()),
    path('loanaccount/<str:pk>/',LoanAccountDetail.as_view()),

    #Loan Payment
    path('loanpayment/',LoanPaymentList.as_view()),
    path('loanpayment/<str:pk>/',LoanPaymentDetail.as_view()),

    # Loan Payment History
    path('loanpaymenthistory/', LoanPaymentHistoryList.as_view()),
    path('loanpaymenthistory/<str:pk>/', LoanPaymentHistoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
