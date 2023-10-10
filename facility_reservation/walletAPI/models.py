from django.db import models
from wallet.models import User  # Import the User model from the "wallet" app
import uuid

class VendorTransaction(models.Model):

    # Choices for currency selection
    CURRENCY_CHOICES = (
        ('points', 'Points'),
        ('coins', 'Coins'),
    )

    # Custom UUID field with the "WILMS" prefix
    reference_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)

    # Foreign keys to User model from the "wallet" app
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming User is the customer

    # Fields for transaction details entered by the user
    transaction_date = models.DateField()
    transaction_id = models.CharField(max_length=255)
    transaction_amount = models.FloatField(default=0.0)

    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default='coins')
   

    def __str__(self):
        return str(self.reference_code)
