from django.db import models

class audImag(models.Model):
    imgtitle = models.CharField(max_length=100)

    input_image = models.ImageField(upload_to="media/input/")
    direct_output_image = models.ImageField(upload_to="media/direct_output/")
    output_image = models.ImageField(upload_to="media/output/")
    songfile = models.FileField(upload_to="media/output/")
