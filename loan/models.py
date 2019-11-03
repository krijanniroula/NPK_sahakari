from django.db import models
from share_member.models import ShareMember
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import *
from datetime import timedelta
from saving_account.models import *

#create loan type
class LoanType(models.Model):
    name = models.CharField(max_length=50)
    interest_rate = models.IntegerField()
    slug = models.SlugField(primary_key=True, unique=True, editable=False)
    createdBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'loan_type'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + "loan")
        print(self.slug)
        super(LoanType, self).save(*args, **kwargs)

def ids():
    no = LoanAccount.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

STATUS_TYPE=(
    ('OPEN','OPEN'),
    ('CLOSED','CLOSED')
)

# loan account creation
class LoanAccount(models.Model):
    id = models.IntegerField(default=ids, unique=True, editable=False)
    share_member = models.ForeignKey(ShareMember, on_delete=models.CASCADE)
    loan_number = models.CharField(max_length=50,primary_key=True,editable=False)

    loan_type = models.OneToOneField(LoanType, on_delete=models.CASCADE)
    status = models.CharField("Status Type",choices=STATUS_TYPE,max_length=50,default="OPEN")

    amount_received = models.DecimalField(max_digits=15,decimal_places=2)
    createdBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,editable=False)
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)
    updatedAt = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.loan_number = "{}{:04d}".format('NPK2017LN', self.id)
        super(LoanAccount, self).save(*args, **kwargs)

    class Meta:
        db_table = 'loan_account'

def loan_payment_ids():
    no = LoanPayment.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

#loan payment detail
class LoanPayment(models.Model):
    id = models.IntegerField(default=loan_payment_ids, editable=False,primary_key=True)
    loan_account = models.ForeignKey(LoanAccount,on_delete=models.CASCADE)
    paid = models.DecimalField(max_digits=15,decimal_places=2)

    createdBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True, editable=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'loan_payment'

def loan_payment_history_ids():
    no = LoanPaymentHistory.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

#loan payment history
class LoanPaymentHistory(models.Model):
    id = models.IntegerField(default=loan_payment_history_ids, editable=False,primary_key=True)
    loan_payment = models.ForeignKey(LoanPayment,on_delete=models.CASCADE)
    date = models.DateField()
    principle = models.DecimalField(max_digits=15,decimal_places=2)
    interest =models.DecimalField(max_digits=15,decimal_places=2)
    paid = models.DecimalField(max_digits=15,decimal_places=2)
    remaining = models.DecimalField(max_digits=15,decimal_places=2)

    createdBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=True)

    # def montly_interest(self):
    #     amount = self.loan_payment.loan_account.amount_received
    #     rate = self.loan_payment.loan_account.loan_type.interest_rate
    #     calc_interest = lambda value: value * rate
    #     monthly = []
    #     for i in range(12):
    #         interest = calc_interest(amount)
    #         amount += interest
    #         monthly.append((i, amount, interest))
    #     return monthly

    def get_interest(self):
        p = self.get_principle()
        r = self.loan_payment.loan_account.loan_type.interest_rate
        t = 1 / (36500)
        return p * Decimal(t) * r


    def get_principle(self):
        no = LoanPaymentHistory.objects.count()
        if no == 0:
            return self.loan_payment.loan_account.amount_received
        else:
            obj = LoanPaymentHistory.objects.get(pk=self.pk-1)
            return obj.remaining

    def save(self, *args, **kwargs):
        self.date = self.loan_payment.createdAt
        self.interest = self.get_interest()
        self.principle = self.get_principle()
        self.paid = self.loan_payment.paid
        principle_with_interest = self.principle + self.interest
        self.remaining = round(principle_with_interest,2) - self.paid
        if self.remaining <= 0.00:
            loan_account = self.loan_payment.loan_account
            loan_account.status = "CLOSED"
            loan_account.save()
        super(LoanPaymentHistory, self).save(*args, **kwargs)

    @receiver(post_save, sender=LoanPayment)
    def create_loan_payment_history(sender, instance, created, **kwargs):
        if created:
           LoanPaymentHistory.objects.create(loan_payment=instance)


    class Meta:
        db_table = 'loan_payment_history'