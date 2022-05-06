from django.db import models

class Quiz(models.Model):
    question_id = models.BigIntegerField()
    text = models.TextField()
    answer = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.question_id
