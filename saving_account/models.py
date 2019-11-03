from django.db import models
from share_member.models import ShareMember
from django.contrib.auth.models import User
from django.utils.text import slugify

ACCOUNT_TYPE=(
    ('-','-'),
    ('DAILY','DAILY'),
    ('MONTHLY','MONTHLY')
)

class SavingType(models.Model): # Normal, Timed, Child
    name = models.CharField(max_length=50)
    # description = models.CharField(null=True,max_length=200)
    account_type = models.CharField("Account Type",choices=ACCOUNT_TYPE,max_length=50,default="-")
    slug = models.SlugField(primary_key=True,unique=True,editable=False)
    interest_rate = models.IntegerField()
    createdBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,editable=False)
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'saving_type'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name+self.account_type)
        print(self.slug)
        super(SavingType, self).save(*args, **kwargs)

def ids():
    no = SavingAccount.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

class SavingAccount(models.Model):
    id = models.IntegerField(default=ids, unique=True, editable=False)
    share_member = models.ForeignKey(ShareMember, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50,primary_key=True,editable=False)
    saving_type = models.OneToOneField(SavingType, on_delete=models.CASCADE)

    time_in_yr = models.IntegerField(null=True)
    createdBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,editable=False)
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)
    updatedAt = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.account_number = "{}{:04d}".format('NPK017GC', self.id)
        super(SavingAccount, self).save(*args, **kwargs)

    class Meta:
        db_table = 'saving_account'


AMOUNT_TYPE=(
    ('Dr','DEBIT'),
    ('Cr','CREDIT')
)

class Saving(models.Model):
    saving_account = models.ForeignKey(SavingAccount, on_delete=models.CASCADE)
    particular = models.CharField(max_length=200,null=True)
    amount = models.IntegerField()

    amount_type = models.CharField("Amount Type",choices=AMOUNT_TYPE,max_length=50)
    createdBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'saving'





