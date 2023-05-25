from django.contrib import admin

# Register your models here.
from .models import Log,userreg,shopreg,workshop,product,order,payment,feedback,notification,complaints,counciling,shop
admin.site.register(Log)
admin.site.register(userreg)
admin.site.register(shopreg)
admin.site.register(workshop)
admin.site.register(product)
admin.site.register(order)
admin.site.register(payment)
admin.site.register(feedback)
admin.site.register(notification)
admin.site.register(complaints)
admin.site.register(counciling)
admin.site.register(shop)