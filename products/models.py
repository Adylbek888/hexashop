from django.db import models

class Womens(models.Model):
    image = models.ImageField(upload_to='static/images')
    name = models.CharField(max_length=120)
    baha = models.CharField(max_length=20)
    description = models.TextField(null=True)


    class Meta:
        verbose_name = 'Women'
        verbose_name_plural = 'Womens'

class Mens(models.Model):
    image = models.ImageField(upload_to='static/images')
    name = models.CharField(max_length=120)
    baha = models.CharField(max_length=20)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'Men'
        verbose_name_plural = 'Mens'

class Kids(models.Model):
    image = models.ImageField(upload_to='static/images')
    name = models.CharField(max_length=120)
    baha = models.CharField(max_length=20)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'Kid'
        verbose_name_plural = 'Kids'

class Accessories(models.Model):
    image = models.ImageField(upload_to='static/images')
    name = models.CharField(max_length=120)
    baha = models.CharField(max_length=20)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'Accessory'
        verbose_name_plural = 'Accessories'