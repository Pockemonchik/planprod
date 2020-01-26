from django.contrib import admin
from plan.models import Profile,Kafedra,Plan,Predmet,UMR,VR,DR,NIR,INR,Nagruzka,DocInfo,Mesyac,Article
class PlanAdmin(admin.ModelAdmin):
    search_fields = ('name',)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('fullname',)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Kafedra)
admin.site.register(Plan,PlanAdmin)
admin.site.register(Predmet)
admin.site.register(UMR)
admin.site.register(VR)
admin.site.register(DR)
admin.site.register(NIR)
admin.site.register(INR)
admin.site.register(Nagruzka)
admin.site.register(DocInfo)
admin.site.register(Mesyac)
admin.site.register(Article)
# Register your models here.
