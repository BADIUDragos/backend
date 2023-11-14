from django.db import models


class TestModel(models.Model):
    test_string = models.CharField(max_length=200)

    def __str__(self):
        return self.test_string
