from django.db import models
class ContactDealer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    item_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

class Meta:
    permissions = [
        ("can_view_contact_dealer", "Can view Contact Dealer"),
        ("can_edit_contact_dealer", "Can edit Contact Dealer"),
    ]
# Create your models here.
