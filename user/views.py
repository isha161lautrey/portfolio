from django.shortcuts import render
from .models import notice

# Create your views here.
def user_home(request):
    imp_notice = notice.objects.filter(is_important=True)
    normal_notice = notice.objects.filter(is_important=False)
    context = {
        'imp_notice' : imp_notice,
        'normal_notice' : normal_notice,
    }
    return render(request, 'user_home/home.html', context)