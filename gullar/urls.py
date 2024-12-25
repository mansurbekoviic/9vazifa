from django.urls import path
from . import views

urlpatterns = [
    path('gullar/', views.barcha_gullar, name='barcha_gullar'),
    path('gullar/tur/<int:tur_id>/', views.gullar_turlar_bo_yicha, name='gullar_turlar_bo_yicha'),
    path('gul/<int:gul_id>/', views.bitta_gul, name='bitta_gul'),
    path('turlar/', views.barcha_turlar, name='barcha_turlar'),
]
