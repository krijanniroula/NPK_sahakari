from NPK_sahakari.models import *
from django.contrib.auth.models import User

class Address(models.Model):
    provision = models.CharField(max_length=100, default="Provision 1")
    district = models.CharField(max_length=50,default='Jhapa')
    municipality = models.CharField(max_length=50,default='Gauradaha')
    ward = models.IntegerField(default=1)
    village = models.CharField(max_length=50, default='Gurung Chowk')

def ids():
    no = ShareMember.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

class ShareMember(PersonDetail,models.Model):
    id = models.IntegerField(default=ids, unique=True, editable=False)
    share_no = models.CharField(max_length=100,primary_key=True, editable=False)

    amount_paid = models.IntegerField(default=100)
    extra_amount = models.IntegerField(default=0)

    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    alternative_person = models.CharField(max_length=100)

    isActive = models.BooleanField(default=True)

    createdBy = models.ForeignKey(User, related_name='member_created_by', null=True,on_delete=models.SET_NULL,editable=False)
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)
    updatedAt = models.DateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        self.share_no = "{}{:02d}".format('NPK', self.id)
        super(ShareMember,self).save(*args,**kwargs)

    class Meta:
        db_table = 'share_member'









