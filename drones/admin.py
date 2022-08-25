from django.contrib import admin
from .models import DroneCategory
from .models import Drone
from .models import Pilot
from .models import Competition
# Register your models here.

admin.site.register(DroneCategory)
admin.site.register(Drone)
admin.site.register(Pilot)
admin.site.register(Competition)
