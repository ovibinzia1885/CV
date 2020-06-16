from django.contrib import admin
from.models import About,Experience,Education,Skill,Interest,Award

class viewabout(admin.ModelAdmin):
    class Meta:
        model=About
    list_display = ('firstName','lastName','email','github',)
admin.site.register(About,viewabout)

class viewexper(admin.ModelAdmin):
    class Meta:
        view=Experience
    list_display = ('title','companyName',)
admin.site.register(Experience,viewexper)

class vieweducation(admin.ModelAdmin):
    class Meta:
        edu=Education
    list_display = ('name','dept','year',)
admin.site.register(Education,vieweducation)

class vieweskil(admin.ModelAdmin):
    class Meta:
        skil=Skill
    list_display = ('mySkill',)
admin.site.register(Skill,vieweskil)

class vieweinterest(admin.ModelAdmin):
    class Meta:
        interest=Interest
    list_display = ('myInterest',)
admin.site.register(Interest,vieweinterest)

class viewawrd(admin.ModelAdmin):
    class Meta:
        awrd=Award
    list_display = ('myAward',)
admin.site.register(Award,viewawrd)