from django.db import models


class Estabelecimento(models.Model):
    cep = models.CharField('CEP', max_length=20)
    nome = models.CharField('Nome', max_length=200)
    logradouro = models.CharField('Logradouro', max_length=300)
    numero = models.CharField('Número', max_length=10)
    bairro = models.CharField('Bairro', max_length=200)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=50)
    pais = models.CharField('País', max_length=60)
    lat = models.CharField('Latitude', max_length=50)
    lon = models.CharField('Longitude', max_length=50)

    class Meta:
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabelecimentos'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
