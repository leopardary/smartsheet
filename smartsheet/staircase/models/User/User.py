from django.db import models

class Group(models.Model):
    group_name=models.CharField(max_length=120)
    parent_group=models.ForeignKey('self',null=True,blank=True)
    note=models.CharField(max_length=500,null=True,blank=True)
    manager=models.ForeignKey('User',on_delete=models.SET_NULL,null=True,blank=True,related_name='groupmanager')
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)    #creation time
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)  #update time
    def __str__(self):
        return self.group_name

class User(models.Model):
    first_name=models.CharField(max_length=120,null=True,blank=True)
    last_name=models.CharField(max_length=120,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    phonenumber=models.CharField(max_length=120,null=True,blank=True)
    group=models.ForeignKey(Group,on_delete=models.SET_NULL,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)    #creation time
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)  #update time
    def __str__(self):
        return self.first_name+'\t'+self.last_name+'\t'
    @classmethod
    def create(cls,first_name,last_name,email,phonenumber,group):
        user=cls(first_name=first_name,last_name=last_name,email=email,phonenumber=phonenumber,group=Group.objects.filter(id=group)[0]);
        user.save()
        return user