from django.contrib import admin

# Register your models here.
from ideas.models import Vote, Idea
from django.utils.html import format_html


#
# admin.site.register(Vote)
# admin.site.register(Idea)

class VoteInline(admin.TabularInline):
    model = Vote


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'show_youtube_url']
    list_filter = ('status',)
    search_fields = ('title',)

    inlines = [VoteInline]

    def show_youtube_url(self, obj):
        if obj.youtube_url:
            return format_html(f"<a href='{obj.youtube_url}'>{obj.youtube_url}</a>")


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
    list_filter = ['idea']
