from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField()

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=250)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    paginas = models.IntegerField()
    isbn = models.CharField(max_length=13, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.titulo