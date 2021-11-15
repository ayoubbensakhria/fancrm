from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin #<-- include django permission framework
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
import static.constants.constants as const 


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True) #<- must be unique
    username = models.CharField(_('username'), max_length=250, unique=True) #
    reference = models.UUIDField(default=uuid.uuid4, editable=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class ServiceFeedBack(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    service = models.CharField(max_length=255, choices=const.SERVICES)
    rating = models.CharField(max_length=255, choices=[(x, x) for x in range(1, 11)])
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=2000)
    last_update = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now=True)  
    
    class Meta:
        verbose_name = _("ServiceFeedBack")
        verbose_name_plural = _("ServiceFeedBacks")

    def __str__(self):
        return "{username} on {servicename}".format(username = self.user.name, 
                                                servicename = self.service)
    def get_absolute_url(self):
        return reverse("serviceFeedBack_detail", kwargs={"pk": self.pk})