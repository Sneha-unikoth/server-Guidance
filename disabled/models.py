from django.db import models

# Create your models here.
class Log(models.Model):
   username=models.CharField(max_length=20,unique=True)
   password=models.CharField(max_length=20,unique=True)
   role=models.CharField(max_length=20)
   def __str__(self):
    return self.username


class userreg(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20) 
    phone=models.CharField(max_length=20)
    login_id=models.OneToOneField(Log,on_delete=models.CASCADE)
    disability=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    role=models.CharField(max_length=10)
    userstatus=models.CharField(max_length=10)
    def __str__(self):
        return self.name  

class shopreg(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    login_id=models.ForeignKey(Log,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    place=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    shopstatus=models.CharField(max_length=20)
    role=models.CharField(max_length=10)
    def __str__(self):
        return self.address

class workshop(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    workstatus=models.CharField(max_length=20)
    user_id=models.ForeignKey(userreg,on_delete=models.CASCADE)
    def __str__(self):
      return self.name

class product(models.Model):
    product_name=models.CharField(max_length=20)
    product_rate=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images')
    description=models.CharField(max_length=80)
    size=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    shop_id=models.ForeignKey(shopreg,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.product_name

class order(models.Model):
    name=models.CharField(max_length=20)
    product_name=models.CharField(max_length=20)
    quantity=models.CharField(max_length=20)
    total_price=models.CharField(max_length=20)
    date=models.DateField(max_length=20)
    user_id=models.ForeignKey(userreg,on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
    def __str__(self):
        return self.date
 
class payment(models.Model):
    username=models.CharField(max_length=20)
    product_name=models.CharField(max_length=20)
    date=models.DateField(max_length=20)
    total_amount=models.CharField(max_length=20)
    user_id=models.ForeignKey(userreg,on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
    def __str__(self):
        return self.payment

class feedback(models.Model):
    name=models.CharField(max_length=20)
    feedback=models.CharField(max_length=30)
    date=models.DateField(max_length=20)
    user_id=models.ForeignKey(userreg,on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
    def __str__(self):
        return self.feedback

class notification(models.Model):
    notification=models.CharField(max_length=30)
    date=models.DateField(max_length=20)
    shop_id=models.ForeignKey(shopreg,on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
    def __str__(self):
        return self.notification

class complaints(models.Model):
    name=models.CharField(max_length=30)
    complaints=models.CharField(max_length=30)
    date=models.DateField(max_length=20)
    user_id=models.ForeignKey(userreg,on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
    def __str__(self):
        return self.complaints

class counciling(models.Model):
    counciling_type=models.CharField(max_length=30)
    date=models.DateField(max_length=20)
    user_id=models.ForeignKey(userreg,on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
    def __str__(self):
        return self.counciling_type


class shop(models.Model):
    name=models.CharField(max_length=30)
    date=models.DateField(max_length=20)
    user_id=models.ForeignKey(userreg,on_delete=models.CASCADE)
    worker_name=models.CharField(max_length=20)
    user_contact=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
   

              
      
        




