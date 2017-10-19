from django.contrib import admin
from django import forms
from .models import User, Item, Category, Quest, Type, ItemQuest, UserQuest, Set, Amiibo, UserAmiibo


admin.site.site_header = 'Administration'


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'updatedDate','createdDate', 'optIn')
    list_filter = ('createdDate', 'username', 'optIn')
    search_fields = ('username', 'fname', 'lname', 'email')

    def full_name(self, obj):
        return obj.fname+' '+obj.lname


class ItemQuestAdminForm(forms.ModelForm):
    item = forms.ModelChoiceField(queryset=Item.objects.order_by('name'))
    quest = forms.ModelChoiceField(queryset=Quest.objects.order_by('quest_name'))

    class Meta:
        model = ItemQuest
        fields = '__all__'


class ItemQuestAdmin(admin.ModelAdmin):
    list_display = ('quest', 'item', 'quantity_required')
    ordering = ['id', ]
    form = ItemQuestAdminForm
    search_fields = ('quest', 'item', 'quantity_required')


class QuestAdmin(admin.ModelAdmin):
    model = Quest
    list_display = ['quest', 'set', 'type']
    #list_display_links = None
    admin_order_field = 'quest_name'
    ordering = ['quest_name', ]
    search_fields = ('quest', 'set', 'type')

    def quest(self, obj):
        return obj.quest_name


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'rupee_val', 'category')
    ordering = ['name', ]


class SetAdmin(admin.ModelAdmin):
    ordering = ['name', ]


class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name', ]


class TypeAdmin(admin.ModelAdmin):
    ordering = ['name', ]


class AmiiboAdmin(admin.ModelAdmin):
    ordering = ['amiibo_name', ]


# class UserAmiiboAdmin(admin.ModelAdmin):
#     ordering = ['amiibo_name', 'bought']


admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Quest, QuestAdmin)
admin.site.register(Type)
admin.site.register(ItemQuest, ItemQuestAdmin)
admin.site.register(UserQuest)
admin.site.register(Set, SetAdmin)
admin.site.register(Amiibo, AmiiboAdmin)
# admin.site.register(UserAmiibo, UserAmiiboAdmin)
