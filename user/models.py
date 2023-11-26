from django.db import models

# Create your models here.

class UserModel(models.Model):
    
    Name = models.CharField(max_length = 255, unique = True)
    Age = models.IntegerField()
    Sex = models.CharField(max_length=1)
    IsDeleted = models.BooleanField(default = False)

    def __str__(self) -> str:
        return f'{self.Name} - {self.Age}' 