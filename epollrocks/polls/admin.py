from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    max_num = 5

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    actions_on_top = False
    inlines = [ChoiceInline]
    fieldsets = [
        ("Question", {"fields": ["question_text"], "description": "test description"}),
        ("Date information", {"fields": ["publish_date"], "classes": ["collapse"]}),
    ]
    list_display = ["question_text", "publish_date", "was_published_recently"]
    list_filter = ["publish_date"]
    search_fields = ["question_text"]

# Register your models here.
# admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)


