from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(LoanType)
admin.site.register(LoanAccount)
admin.site.register(LoanPayment)
admin.site.register(LoanPaymentHistory)