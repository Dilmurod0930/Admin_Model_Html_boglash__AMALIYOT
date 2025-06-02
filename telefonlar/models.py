from django.db import models

# Create your models here.
class Telefon(models.Model):
    name = models.CharField("Telefon nomi", max_length=100)
    model = models.CharField("Model", max_length=100)
    company = models.CharField("Kompaniya", max_length=100)
    color = models.CharField("Rangi", max_length=50)
    price = models.DecimalField("Narxi (so‘m)", max_digits=12, decimal_places=2)
    storage = models.IntegerField("Xotira (GB)")
    ram = models.IntegerField("RAM (GB)")
    os = models.CharField("Operatsion tizim", max_length=50)
    image = models.ImageField("Telefon rasmi", upload_to='telefonlar/', null=True, blank=True)
    description = models.TextField("Qo‘shimcha ma’lumot", null=True, blank=True)
    created_at = models.DateTimeField("Qo‘shilgan vaqt", auto_now_add=True)
    updated_at = models.DateTimeField("O‘zgartirilgan vaqt", auto_now=True)

    class Meta:
        verbose_name = "Telefon"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} {self.company} {str(self.price)}"