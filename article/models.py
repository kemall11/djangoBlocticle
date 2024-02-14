from django.db import models
from ckeditor.fields import RichTextField 
class article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=50,verbose_name="Başlık")
    text=RichTextField()
    datetime=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    article_image=models.FileField(blank=True,verbose_name="Dosyayı Bırak",null=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-datetime']
class comments(models.Model):
    article=models.ForeignKey(article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author=models.CharField(max_length=25,verbose_name="İsim")
    comment_content=models.TextField(max_length=250,verbose_name="İçerik")
    comment_date=models.DateTimeField( auto_now_add=True )
    def __str__(self):
        return self.comment_author 
    class Meta:
        ordering = ['-comment_date']