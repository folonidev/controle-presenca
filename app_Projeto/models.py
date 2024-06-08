# myapp/models.py
from django.db import models
from django.utils import timezone

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.nome

class Presenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='presencas')
    data = models.DateField(auto_now_add=True)
    presente = models.BooleanField(default=False)

    class Meta:
        ordering = ['-data']
        unique_together = ('aluno', 'data')

    def __str__(self):
        return f"{self.aluno.nome} - {'Presente' if self.presente else 'Ausente'} em {self.data}"

    @property
    def classe_presenca(self):
        return 'presente' if self.presente else 'ausente'

class RegistroPresenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    presente = models.BooleanField(default=False)

    class Meta:
        unique_together = ('aluno', 'data')

    def __str__(self):
        return f"{self.aluno.nome} - {self.data} - {'Presente' if self.presente else 'Ausente'}"

