from django.db import models
# from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model


class Article(models.Model):
    title = models.CharField(verbose_name='عنوان' ,max_length=200, null=False, blank=False)
    body = models.TextField(verbose_name='توضیحات')
    article_file = models.FileField(verbose_name='فایل', upload_to ='uploads/', null=False, blank=False)
    department = models.CharField(verbose_name='نام گروه ', max_length=256,)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        verbose_name='کاربر',
        on_delete=models.CASCADE,
        # related_name= 'author',
    )
    supervisor = models.CharField(verbose_name='استاد راهنما', max_length=256, null=False, blank=False)
    supervisor_approve = models.BooleanField(verbose_name='تایید استاد راهنما')
    head_of_department_approve = models.BooleanField(verbose_name='تایید مدیر گروه')
    department_approve = models.BooleanField(verbose_name='تایید گروه')
    deputy_of_education_approve = models.BooleanField(verbose_name='تایید معاونت آموزشی ')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    
    
professors = (
    ("supervisor", "استاد راهنما"),
    ("head_of_department", "مدیر گروه"),
    ("deputy_of_education", "معاونت آموزشی"),
    ("professor", "استاد گروه "),
)

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete= models.CASCADE,
        related_name= 'comments'
        
        )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # author = models.CharField(verbose_name='', max_length=256, choices=professors)

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("article_list")
    
        