from django.contrib import admin
from .models import Meal, Rating

# Register your models here.
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'meal', 'user', 'stars')
    list_filter = ('meal','user')
    search_fields = ('meal__title', 'user__username')
    
    
    
@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title','description')
    list_filter = ('title','description')