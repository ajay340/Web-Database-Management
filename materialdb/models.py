from django.db import models

class userdb(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    salary = models.CharField(max_length=10)

    def __str__(self):
        return self.num_ID
        return self.name
        return self.country
        return self.city
        return self.salary
