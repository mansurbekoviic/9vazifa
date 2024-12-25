from django.shortcuts import render, get_object_or_404
from .models import Tur, Gul

def barcha_gullar(request):
    gullar = Gul.objects.all()
    return render(request, 'gullar/barcha_gullar.html', {'gullar': gullar})

def gullar_turlar_bo_yicha(request, tur_id):
    gullar = Gul.objects.filter(tur_id=tur_id)
    return render(request, 'gullar/gullar_turlar_bo_yicha.html', {'gullar': gullar})

def bitta_gul(request, gul_id):
    gul = get_object_or_404(Gul, id=gul_id)
    return render(request, 'gullar/bitta_gul.html', {'gul': gul})

def barcha_turlar(request):
    turlar = Tur.objects.all()
    return render(request, 'gullar/barcha_turlar.html', {'turlar': turlar})
