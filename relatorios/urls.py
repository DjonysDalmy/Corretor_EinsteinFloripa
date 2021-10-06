from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('envia_relatorios', views.envia_relatorios, name='envia_relatorios'),
    path('atualiza_pagina_ajax', views.atualiza_pagina_ajax, name='atualiza_pagina_ajax'),
    path('exporta_pdf', views.exporta_pdf, name='exporta_pdf'),
    path('limpa_media', views.limpa_media, name='limpa_media')
]