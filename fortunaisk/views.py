# fortunaisk/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import FortuneRecord

@login_required
def index(request):
    fortunes = FortuneRecord.objects.filter(user=request.user)
    return render(request, 'fortunaisk/index.html', {
        'fortunes': fortunes
    })
