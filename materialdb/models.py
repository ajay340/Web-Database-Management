from django.db import models

class PersonManager(models.Manager):
    def create_user(self, first_name, last_name, country, city, salary):
        user = self.model(first_name=first_name, last_name=last_name, country=country, city=city, salary=salary)
        user.save(using=self._db)
        return user
    def save(self):
        self.filter

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    salary = models.PositiveIntegerField()
    objects = PersonManager()

    def __str__(self):
        return ("%s, %s, %s, %s, %s", self.num_ID, self.first_name, self.country, self.city, self.salary)

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
    
