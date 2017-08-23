from django.contrib import admin
from .models import User, Item, Category, Quest, Type, ItemQuest, UserQuest, Group

admin.site.site_header = 'Administration'


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'updatedDate','createdDate', 'optIn')
    list_filter = ('createdDate', 'username', 'optIn')
    search_fields = ('username', 'fname', 'lname', 'email')

    def full_name(self, obj):
        return obj.fname+' '+obj.lname


class ItemQuestAdmin(admin.ModelAdmin):
    list_display = ('quest_id', 'item_id', 'quantity_required')


class QuestAdmin(admin.ModelAdmin):
    model = Quest
    list_display = ['quest',]
    admin_order_field = 'quest_name'
    ordering = ['quest_name',]

    def quest(self, obj):
        return obj.quest_name


admin.site.register(User, UserAdmin)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Quest, QuestAdmin)
admin.site.register(Type)
admin.site.register(ItemQuest, ItemQuestAdmin)
admin.site.register(UserQuest)
admin.site.register(Group)
