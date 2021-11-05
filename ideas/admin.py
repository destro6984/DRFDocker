from django.contrib import admin

# Register your models here.
from ideas.models import Vote, Idea


#
# admin.site.register(Vote)
# admin.site.register(Idea)

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    pass

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass

