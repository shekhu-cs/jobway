from django.db import models


class coforms(models.Model):
    name = models.CharField(max_length=20)
    website = models.CharField(max_length=20)
    role = models.CharField(max_length=15)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name + self.website + self.description + self.role

    class Meta:
        db_table = 'coforms'
