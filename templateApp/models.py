from django.db import models


class templateModel(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

# Model Field Reference: https://docs.djangoproject.com/en/3.0/ref/models/fields/

# Linha de texto:	models.CharField(max_length=XXX)
# Sim / Não:		models.BooleanField()
# Campos de Texto:	models.TextField()
# Imagens:			models.ImageField(upload_to='/static/uploads')
# Relacionamento:	models.ForeignKey(NOME_MODELO, on_delete=PROTECT)
