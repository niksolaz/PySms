from django.db import models

# Create your models here.
class Sms(models.Model):
	text = models.CharField(max_length=160)
	number = models.CharField(max_length=50)

	def __unicode__(self):
		return "%s ===> %s" % (self.number, self.text)
		