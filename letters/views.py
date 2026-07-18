from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
import openpyxl
from .models import Letter
from .forms import LetterForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'letters/change_password.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        messages.success(self.request, "ይለፍ ቃልዎ በትክክል ተቀይሯል!")
        return super().form_valid(form)
    
    # 1. የደብዳቤ ማስተካከያ (Edit View)
def edit_letter(request, letter_id):
    letter = get_object_or_404(Letter, id=letter_id)
    if request.method == "POST":
        form = LetterForm(request.POST, request.FILES, instance=letter)
        if form.is_valid():
            form.save()
            messages.success(request, "ደብዳቤው በትክክል ተስተካክሏል!")
            return redirect('dashboard')
    else:
        form = LetterForm(instance=letter)
    return render(request, 'letters/edit_letter.html', {'form': form, 'letter': letter})
# 2. የደብዳቤ ማጥፊያ (Delete View)

def delete_letter(request, letter_id):
    letter = get_object_or_404(Letter, id=letter_id)
    letter.delete()
    return redirect('dashboard')

@login_required
def dashboard(request):
    # መፈለጊያ ሳጥን (Search Bar) መረጃ ለማጣራት
    query = request.GET.get('q', '')
    if query:
        letters = Letter.objects.filter(
            Q(letter_number__icontains=query) |
            Q(sender__icontains=query) |
            Q(subject__icontains=query) |
            Q(assigned_to__icontains=query)
        )
    else:
        letters = Letter.objects.all()
        
    form = LetterForm()
    return render(request, 'letters/dashboard.html', {'letters': letters, 'form': form, 'query': query})

@login_required
def create_letter(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return redirect('dashboard')

@login_required
def export_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Letters Report"
    
    headers = ['የደብዳቤ ቁጥር', 'ላኪ (መሥሪያ ቤት)', 'ጉዳዩ/ርዕስ', 'የተመራለት ሰው/ክፍል', 'የተመራበት ቀን', 'ደረጃ', 'ማብራሪያ']
    ws.append(headers)
    
    letters = Letter.objects.all()
    for letter in letters:
        ws.append([
            letter.letter_number,
            letter.sender,
            letter.subject,
            letter.assigned_to,
            letter.assign_date.strftime('%Y-%m-%d') if letter.assign_date else '',
            letter.get_status_display(),
            letter.description if letter.description else ''
        ])
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="letters_report.xlsx"'
    wb.save(response)
    return response