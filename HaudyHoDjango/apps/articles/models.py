import datetime
from django.db import models

from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField("Article's name", max_length=200)
    article_text = models.TextField("Article's text")
    article_publication_date = models.DateTimeField("Article publication date")
    
    def __str__(self):
        return self.article_title
    
    def was_published_resently(self):
        return self.article_publication_date >= (timezone.now() - datetime.timedelta(days = 7))
    
    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"
    
    
class Comment(models.Model):
    comment_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_author = models.CharField("Comment's author", max_length=50)
    comment_text = models.CharField("Comment's text", max_length=200)
    
    def __str__(self):
        return self.comment_author
    
    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
    

    
