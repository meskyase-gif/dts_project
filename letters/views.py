from django.shortcuts import render, redirect
from .models import Letter

def dashboard(request):
    if request.method == "POST":
        letter_number = request.POST.get('letter_number')
        received_date = request.POST.get('received_date')
        sender = request.POST.get('sender')
        subject = request.POST.get('subject')
        assigned_to = request.POST.get('assigned_to')
        status = request.POST.get('status')
        description = request.POST.get('description')
        assign_date = request.POST.get('assign_date')
        assigned_by = request.POST.get('assigned_by')

        # መረጃውን ዳታቤዝ ውስጥ መመዝገብ
        Letter.objects.create(
            letter_number=letter_number,
            received_date=received_date,
            sender=sender,
            subject=subject,
            assigned_to=assigned_to,
            status=status,
            description=description,
            assign_date=assign_date,
            assigned_by=assigned_by
        )
        return redirect('dashboard')

    # የፍለጋ Logic
    search_query = request.GET.get('search_query', '')
    if search_query:
        all_letters = Letter.objects.filter(
            letter_number__icontains=search_query
        ) | Letter.objects.filter(
            sender__icontains=search_query
        ) | Letter.objects.filter(
            subject__icontains=search_query
        )
    else:
        all_letters = Letter.objects.all().order_by('-id')

    context = {
        'letters': all_letters,
        'search_query': search_query
    }
    return render(request, 'letters/dashboard.html', context)