from django.contrib import admin

from .models import Question, Choice
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
				('Question',         {'fields': ['question_text']}),
				('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	] 

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
