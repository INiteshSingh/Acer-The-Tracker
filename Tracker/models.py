from django.db import models

# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    income = models.FloatField()

    def __str__(self):
        return self.name


# class Expense(models.Model):
#     user = models.ForeginKey(UserData, on_delete=models.CASCADE)
#     expense_name = models.CharField(max_lenght=100)
#     amount = models.FloatField()

#     def __str__(self):
#         return f"{self.expense_name}-{self.amount}"