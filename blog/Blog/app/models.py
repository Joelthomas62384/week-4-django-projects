from django.db import models

class About(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    about = models.TextField()

    class Meta:
        verbose_name_plural = "About"
   

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise ValueError('There is already an About instance. Only one instance is allowed.')
        return super(About, self).save(*args, **kwargs)

   

    def __str__(self):
        return self.name
