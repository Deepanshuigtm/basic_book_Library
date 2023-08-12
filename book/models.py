from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.utils.text import slugify # it transform string to a slug like Harry Potter 1 => harry-potter-1

# Create your models here.

# deleting =https://docs.djangoproject.com/en/3.1/topics/db/queries/#deleting-objects
# update = https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-update
# create = https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-create

class Country(models.Model):
    name = models.CharField(max_length=100);
    code= models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.name}, {self.code}"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.fullname()

class Book(models.Model):
    title = models.CharField('title', max_length=100)
    ratings = models.IntegerField([MinValueValidator(1),MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True,related_name="books")
    is_bestselling = models.BooleanField(default=False) 
    slug = models.SlugField(default='',null=False,db_index=True) # harry potter 1 => harry-potter-1
    published_countries = models.ManyToManyField(Country, null=False)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)  # it transform string to a slug like Harry Potter 1 => harry-potter-1
    #     super().save(*args, **kwargs)
        # Book.objects.get(title="harry poter").save()
        # Book.objects.get(title="harry potter").slug => 'harry-potter'

    def __str__(self):
        return f"{self.title} ({self.ratings}) author {self.author} and bestselling {self.is_bestselling}"