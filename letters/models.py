from django.db import models
from django.utils import timezone

class Letter(models.Model):
    STATUS_CHOICES = [
        ('new', 'አዲስ'),
        ('in_progress', 'በሂደት ላይ'),
        ('completed', 'ተጠናቋል'),
    ]

    letter_number = models.CharField(max_length=100, verbose_name="የደብዳቤ ቁጥር")
    received_date = models.DateField(default=timezone.now, verbose_name="ደብዳቤው የገባበት ቀን")
    sender = models.CharField(max_length=255, verbose_name="ላኪ (መሥሪያ ቤት)")
    subject = models.CharField(max_length=255, verbose_name="ጉዳይ/ርዕስ")
    assigned_to = models.CharField(max_length=255, verbose_name="የተመራለት ሰው/ክፍል")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="ደረጃ")
    description = models.TextField(blank=True, null=True, verbose_name="ማብራሪያ")
    
    # አዳዲስ የተጨመሩት
    assign_date = models.DateField(default=timezone.now, verbose_name="ደብዳቤው የተመራበት ቀን")
    assigned_by = models.CharField(max_length=255, verbose_name="ደብዳቤውን የመራው ኃላፊ")
    scanned_copy = models.FileField(upload_to='scanned_letters/', null=True, blank=True)

    def __str__(self):
        return f"{self.letter_number} - {self.subject}"