from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

	url(r'^templateView/', views.templateView, name="templateView"),
]

# URL com REGEX para buscar apenas um resultado
# url(r'^DETALHE/(?P<identificador>\w+)', views.DETALHE, name="DETALHE"),