from django.contrib import admin
from . models import User, Truck, Category, Color

# Register your models here.

admin.site.register(User)
admin.site.register(Truck)
admin.site.register(Category)
admin.site.register(Color)
