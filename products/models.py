from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
    ("F", "Fruit"), # 한 글자는 DB에 저장, 단어는 사용자에게 보여질 단어
    ("V", "Vegetable"),
    ("M", "Meat"),
    ("O", "Other"),
)
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField() # 정수값만
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name