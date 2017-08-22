from django.contrib import admin
from .models import User, Item, Category

admin.site.site_header = 'Administration'

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'updatedDate','createdDate', 'optIn')
    list_filter = ('createdDate', 'username', 'optIn')
    search_fields = ('username', 'fname', 'lname', 'email')

    def full_name(self, obj):
        return obj.fname+' '+obj.lname

class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Item)
admin.site.register(Category)
