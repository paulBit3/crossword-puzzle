from django.contrib import admin

from .models import *

# Register your models here.


class PuzzleAdmin(admin.ModelAdmin):
    list_display = ['title', 'byline', 'publisher']
    list_filter = ['date']



class ClueAdmin(admin.ModelAdmin):
    list_display = ['entry', 'puzzle', 'clue_text']
    list_filter = ['theme']



# Registering our models.
admin.site.register(Puzzle, PuzzleAdmin)
admin.site.register(Entry)
admin.site.register(Clue, ClueAdmin)