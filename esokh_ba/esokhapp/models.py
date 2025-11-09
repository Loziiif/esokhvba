from django.db import models
from django.contrib.auth.models import AbstractUser


# 👤 Custom User model (Role бүхий)
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('ajiltan', 'СӨХ-ийн ажилтан'),
        ('orshinsuu', 'Оршин суугч'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='orshinsuu')

    def __str__(self):
        return f"{self.username} ({self.role})"


# 🏢 СӨХ байгууллага
class Soh(models.Model):
    ner = models.CharField(max_length=200)
    hayg = models.CharField(max_length=300)
    utas = models.CharField(max_length=20)
    email = models.EmailField()
    uusgesen_ognoo = models.DateTimeField(auto_now_add=True)

    # СӨХ-ийн ажилтнууд
    ajiltanuud = models.ManyToManyField(User, related_name='hariyalah_soh', limit_choices_to={'role': 'ajiltan'}, blank=True)

    def __str__(self):
        return self.ner


# 🧍‍♂️ Оршин суугч
class Orshinsuu(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'orshinsuu'})
    soh = models.ForeignKey(Soh, on_delete=models.CASCADE, related_name='orshinsuud')
    bair_dugaar = models.CharField(max_length=10)
    utas = models.CharField(max_length=20)
    orshin_baigaa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} ({self.soh.ner})"


# 💵 Төлбөрийн төрөл
class TulburTuriinAngilal(models.Model):
    ner = models.CharField(max_length=100)
    tailbar = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ner


# 💳 Төлбөрийн бүртгэл
class Tulbur(models.Model):
    orshinsuu = models.ForeignKey(Orshinsuu, on_delete=models.CASCADE, related_name='tulburuud')
    tulbur_turul = models.ForeignKey(TulburTuriinAngilal, on_delete=models.SET_NULL, null=True, blank=True)
    sar = models.CharField(max_length=20)  # Ж: "2025-11"
    dun = models.DecimalField(max_digits=10, decimal_places=2)
    tulbur_tulsun = models.BooleanField(default=False)
    tulbur_ognoo = models.DateField(null=True, blank=True)
    tulbur_barimt = models.FileField(upload_to='barimt/', null=True, blank=True)

    def __str__(self):
        return f"{self.orshinsuu.user.username} - {self.sar}"


# 📢 Notification / мэдэгдэл
class Notification(models.Model):
    soh = models.ForeignKey(Soh, on_delete=models.CASCADE, related_name='medegdluud')
    ilgeesen_ajiltan = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ilgeesen_medegdluud', limit_choices_to={'role': 'ajiltan'})
    garchig = models.CharField(max_length=200)
    aguulga = models.TextField()
    ognoo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.garchig} ({self.soh.ner})"


# 📋 Төлбөрийн нэхэмжлэл (invoice)
class Nehemjlel(models.Model):
    ajiltan = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nehemjlel_ilgeesen', limit_choices_to={'role': 'ajiltan'})
    orshinsuu = models.ForeignKey(Orshinsuu, on_delete=models.CASCADE, related_name='nehemjlel_avsan')
    sar = models.CharField(max_length=20)
    dun = models.DecimalField(max_digits=10, decimal_places=2)
    ognoo = models.DateTimeField(auto_now_add=True)
    tulbur_hiisen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.orshinsuu.user.username} - {self.sar}"


# 💬 Санал хүсэлт
class Sanal(models.Model):
    orshinsuu = models.ForeignKey(Orshinsuu, on_delete=models.CASCADE, related_name='sanaluud')
    aguulga = models.TextField()
    ognoo = models.DateTimeField(auto_now_add=True)
    harasan = models.BooleanField(default=False)

    def __str__(self):
        return f"Sanal - {self.orshinsuu.user.username}"
