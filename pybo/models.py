from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    # models.CASCADE 글쓴이가 삭제되면 Question 모델도 같이 사라짐.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    # balck=True form.is_valid()를 통한 입력 폼 데이터 검사 시 값이 없어도 된다는 의미.
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
