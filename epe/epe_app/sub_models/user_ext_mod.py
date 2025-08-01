from django.contrib.auth.models import User
from django.db import models
from epe.epe_app.models import RoleInfo

class User_extInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    emp_role = models.ForeignKey(RoleInfo, on_delete=models.CASCADE, null=True,blank=True)


    def __str__(self):
        return self.user.username