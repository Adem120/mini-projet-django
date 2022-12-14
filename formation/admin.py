from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from formation.models import Experience, Skills, Type, Diplome

# Register your models here.
class DiplomAdmin(admin.ModelAdmin):
    liste_display=('diplome','date','type')
    def Type_link(self,diplome):
        return mark_safe('<a href="{}">{}</a>'.format(reverse("admin:Drugs_Type_change", Diplome=(diplome.Type.pk,)),diplome.Type.TypeName ))
class TypeAdmin(admin.ModelAdmin):
    list_display=('TypeName','description')
    def apercu (self, Type):
        text = Type.description[:40]
        if len(Type.description) > 40:
            return '{}...'.format(text)
        else:
            return text
class SkillsAdmin(admin.ModelAdmin):
    liste_display=('skills','perc')
class ExperienceAdmin(admin.ModelAdmin):
    liste_display=('experience','datedebut','datefin')
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Skills,SkillsAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Diplome, DiplomAdmin)