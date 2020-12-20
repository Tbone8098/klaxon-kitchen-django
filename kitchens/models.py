from django.db import models

# Create your models here.
class KitchenManager(models.Manager):
    def kitchen_validator(self, postData):
        errors = {}
        if Kitchen.objects.filter(name=postData['kitchen_name']):
            errors['nameExistenceError'] = "That Kitchen name already exists"
        if len(postData['kitchen_name']) < 8:
            errors['nameLenError'] = "The Name of the Kitchen needs to be at least 8 characters"
        if Kitchen.objects.filter(designation_id=postData['designationId']):
            errors['desigExistenceError'] = "That Designation already exists"

        return errors

class OrderManager(models.Manager):
    def order_validator(self, postData):
        errors = {}
        # if postData['orderNum'] == None:
        #     errors['orderNumError'] = "Must enter a Order Number"
        # if postData['kitchen_name'] == None:
        #     errors['kitchenChoiceError'] = "Must select a Kitchen"
        
        return errors



class Kitchen(models.Model):
    name = models.CharField(max_length=255)
    designation_id = models.CharField(max_length=255)
    daily_order_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = KitchenManager()

class Order(models.Model):
    order_num = models.CharField(max_length=255)
    notes = models.TextField()
    status = models.CharField(max_length=255)
    kitchen = models.ForeignKey(Kitchen, related_name="orders", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OrderManager()
