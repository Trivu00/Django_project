from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Thể loại của bài đọc')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categores'

class ReadingBook(models.Model):
    name = models.CharField(max_length=200, help_text='Tên bài đọc')
    read_write = models.TextField(help_text='Nội dung bài đọc')
    name_id = models.CharField(max_length=10, help_text='ID của bài đọc')
    author = models.CharField(max_length=100, help_text='Tên tác giả', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    def __str__(self):
        return self.name

