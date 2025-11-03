<<<<<<< HEAD
from django.db import models

# Form model with Image field to be uploaded.
class Sign(models.Model):
=======
from django.db import models

# Form model with Image field to be uploaded.
class Sign(models.Model):
>>>>>>> 32192d3fad935538ba576886e60de0cb84432f60
	gesture = models.ImageField(upload_to='',blank=False)