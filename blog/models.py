from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Tag(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Comment(models.Model):
	name = models.CharField(max_length=30)
	body = models.CharField(max_length=100)
	date = models.DateTimeField()

	def __str__(self):
		return self.name

class Blog(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=800)
    date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    comments = models.ManyToManyField(Comment)
        


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
