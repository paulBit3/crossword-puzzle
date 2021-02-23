from django.db import models
from datetime import datetime
from django.urls import reverse



# Defining the xword data model


class Puzzle(models.Model):
    """Puzzle class"""
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    byline = models.CharField(max_length=255)
    publisher = models.CharField(max_length=12)

    class meta:
        ordering = ['-date']
    
    def get_puzzle(self):
        if self.title:
            return self.title
    

    def datepublished(self):
        return self.date.strftime('%Y-%m-%d')


    def __str__(self):
        return f'{self.title}'
    
    # returning the path of the url
    def get_absolute_url(self):
        return reverse('puzzle:puzzle_details', kwargs={'pk': self.id})



class Entry(models.Model):
    """Entry class"""
    entry_text = models.CharField(max_length=50)

    class meta:
        ordering = ['-entry_text']
    
    def __str__(self):
        return self.entry_text
    
    # returning the length of the entry
    def __len__(self):
        return len(self.entry_text)



class Clue(models.Model):
    """Clue class"""
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    clue_text = models.CharField(max_length=512)
    theme = models.BooleanField(default=False)

    class meta:
        unique_together = ('entry', 'puzzle',)
    
    def __str__(self):
        return '%s %s %f' % (self.entry, self.puzzle, self.clue_text)