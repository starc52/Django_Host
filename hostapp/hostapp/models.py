from django.db import models
from django.core.files.base import ContentFile
import os

class audImag(models.Model):
	imgtitle = models.CharField(max_length=100)

	input_image = models.ImageField(upload_to="media/input/")
	direct_output_image = models.ImageField(upload_to="media/direct_output/")
	output_image = models.ImageField(upload_to="media/output/")
	songfile = models.FileField(upload_to="media/output/")

def prepare():
	mypath="/ug/ug2k18/cse/sai.tanmay/rand/ssd_scratch/cvit/starc52/VoxCeleb2/test_relocated/data/output_frames/"
	onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

	list_of_names = [i[:-4] for i in onlyfiles]
	cropped_path="/ug/ug2k18/cse/sai.tanmay/rand/ssd_scratch/cvit/starc52/VoxCeleb2/test_relocated/data/cropped_frames/"
	output_path="/ug/ug2k18/cse/sai.tanmay/rand/ssd_scratch/cvit/starc52/VoxCeleb2/test_relocated/data/output_frames/"
	audios_path="/ug/ug2k18/cse/sai.tanmay/rand/ssd_scratch/cvit/starc52/VoxCeleb2/test_relocated/data/audios/"
	direct_output_path="/ug/ug2k18/cse/sai.tanmay/rand/ssd_scratch/cvit/starc52/VoxCeleb2/test_relocated/data/direct_output_frames/"

	for i in list_of_names:
		f = open(cropped_path+i+".jpg", "rb")
		f1 = open(output_path+i+".jpg", "rb")
		f2 = open(audios_path+i+".wav", "rb")
		f3 = open(direct_output_path+i+".jpg", "rb")

		record = audImag()
		record.imgtitle=i+".jpg"
		record.input_image.save(i+".jpg", ContentFile(f.read()))
		record.direct_output_image.save(i+".jpg", ContentFile(f3.read()))
		record.output_image.save(i+".jpg", ContentFile(f1.read()))
		record.songfile.save(i+".wav", ContentFile(f2.read()))
		f.close()
		f1.close()
		f2.close()
		f3.close()
