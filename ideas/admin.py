from django.contrib import admin
from .models import Idea, Category,Person, Document ,Comment

class IdeaAdmin(admin.ModelAdmin):
    list_display=("title","created_at","is_active")
    list_filter = ("title","created_at","is_active")

class CommentAdmin(admin.ModelAdmin):
    list_display=("full_name","idea","created_at")
    list_filter = ("full_name","idea","created_at")

admin.site.register(Idea,IdeaAdmin)
admin.site.register(Category)
admin.site.register(Person)
admin.site.register(Document)
admin.site.register(Comment,CommentAdmin)
