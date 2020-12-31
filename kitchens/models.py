from django.db import models

# Create your models here.
class KitchenManager(models.Manager):
    def kitchen_validator(self, postData):
        errors = {}
        if Kitchen.objects.filter(name=postData['kitchen_name']):
            errors['nameExistenceError'] = "That Kitchen name already exists"
        if len(postData['kitchen_name']) < 3:
            errors['nameLenError'] = "The Name of the Kitchen needs to be at least 8 characters"
        if Kitchen.objects.filter(designation_id=postData['designationId']):
            errors['desigExistenceError'] = "That Designation already exists"

        return errors

class OrderManager(models.Manager):
    def Order_validator(self, postData):
        errors = {}
        if len(postData['orderNum']) < 1:
            errors['orderNumLenError'] = "You must enter an order number"
        
        return errors


class Kitchen(models.Model):
    name = models.CharField(max_length=255)
    designation_id = models.CharField(max_length=255)
    daily_order_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = KitchenManager()

class Order(models.Model):
    ticket_num = models.CharField(max_length=255, default="0000")
    order_num = models.CharField(max_length=255)
    notes = models.TextField()
    status = models.CharField(max_length=255)
    kitchen = models.ForeignKey(Kitchen, related_name="orders", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OrderManager()
