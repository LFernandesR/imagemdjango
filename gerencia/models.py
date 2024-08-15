from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=100)
    data_nasc = models.DateField()
    imagem = models.ImageField(upload_to='alunosimg/')

    def __str__(self):
        return self.nome
    


