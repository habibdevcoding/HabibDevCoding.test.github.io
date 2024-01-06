from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# admin.site.register(Question)



# class ChoiceInline(admin.StackedInline):
#     model = Choice 
#     extra = 3
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice 
    extra = 3
admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin): 
    fieldsets = [ 
        (None, {'fields': ['question_text']}), 
        ('Date information', {'fields': ['pub_date'], 
        'classes': ['collapse']}), ] 
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)


