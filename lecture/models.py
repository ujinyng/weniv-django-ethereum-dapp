from django.db import models
from taggit.managers import TaggableManager

class Lecture(models.Model):
	leName = models.CharField(max_length=50)
	lePlace = models.TextField(blank=True, null=True)
	leIntroduce = models.TextField()
	leSimpleIntroduce = models.TextField(max_length=100, blank=True, null=True)
	lePhoto = models.ImageField(blank=True, null=True)
	lePu = models.DateTimeField(blank=True, null=True)
	leMo = models.DateTimeField(blank=True, null=True)
	leMento = models.CharField(max_length=20)
	tag = TaggableManager(blank=True)
	
	def __str__(self):
		return self.leName
