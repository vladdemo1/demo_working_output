"""
This mod contains main model for this project
"""

from django.db import models
from django.urls import reverse


def get_worker_url(obj, viewname):
    """
    get worker url by position and name
    """
    # ct_model = obj.__class__._meta.model_name
    # 'ct_model': ct_model, 
    return reverse(viewname, kwargs={'position': obj.position, 'first_name': obj.first_name, 'last_name': obj.last_name})


class Worker(models.Model):
    """
    Main worker model

        Parameters
        ----------
        first_name : str
            Worker's first name

        middle_name : str
            Worker's middle name

        last_name : str
            Worker's last name

        position : str
            Working rank

        date_of_receipt : datetime
            Worker's date of receipt to work

        email : email
            Email of worker

        boss : fk
            Node to once boss
    """
    first_name = models.CharField(max_length=24, verbose_name="Ім'я")
    middle_name = models.CharField(max_length=24, verbose_name="По батькові")
    last_name = models.CharField(max_length=24, verbose_name="Прізвище")

    position = models.CharField(max_length=48, verbose_name="Посада")

    date_of_receipt = models.DateTimeField(auto_now=True, null=True)

    email = models.EmailField(verbose_name="Email", unique=True)
    boss = models.ForeignKey('self', verbose_name='Начальник', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        """
        Get worker's first name with position
        """
        return f"{self.first_name} [{self.position}]"

    def get_absolute_url(self):
        """
        get url by position and name
        """
        return get_worker_url(self, 'worker-detail')
    

    class Meta:
        verbose_name_plural = 'Працівник'
