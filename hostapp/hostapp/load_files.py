from hostapp.models import audImag
from django.db import models
import os

mypath="/home/starc/Desktop/"
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

if 