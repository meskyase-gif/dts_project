from django import forms
from .models import Letter

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        # 'scanned_copy' እዚህ ጋር ተጨምሯል
        fields = ['letter_number', 'sender', 'subject', 'assigned_to', 'status', 'description', 'assigned_by', 'scanned_copy']
        
        widgets = {
            'letter_number': forms.TextInput(attrs={'class': 'form-control'}),
            'sender': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'assigned_to': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'assigned_by': forms.TextInput(attrs={'class': 'form-control'}),
            # ለፋይል መጫኛ ዊጄት መጨመር ትችላለህ (አማራጭ ነው)
            'scanned_copy': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }