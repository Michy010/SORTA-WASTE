from django.db import models
from accounts.models import CustomUser

class WasteOrder (models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    WASTE_CHOICES = [
        ('plastic', 'Plastic Waste'),
        ('organic', 'Organic Waste'),
        ('metallic', 'Metallic Waste'),
        ('electronic', 'Electronic Waste'),
    ]
    waste_type = models.CharField(max_length=20, choices=WASTE_CHOICES, default='plastic')
    bin_picture = models.ImageField(upload_to = 'bin_picture/', null=True, blank=True)
    WASTE_CHOICES = [
        ('small', '5Kg'),
        ('medium', '10Kg'),
        ('large', '15Kg'),
        ('super', '20Kg'),
    ]
    size = models.CharField(max_length=10, choices=WASTE_CHOICES, default='5Kg')

    def __str__(self):
        return f"Order {self.id}"