from django.shortcuts import render
from loans.models import Loan
from django.utils import timezone

def generate_report(request):
    report = None

    if 'start_date' in request.GET and 'end_date' in request.GET:
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        # Filtra os empréstimos com base no intervalo de datas
        report = Loan.objects.filter(loan_date__gte=start_date, loan_date__lte=end_date)

    return render(request, 'report_form.html', {
        'report': report
    })