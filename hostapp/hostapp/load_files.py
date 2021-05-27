from models import audImag
from django.core.files import File
from django.db import models
#from django.conf import settings
settings.configure()
import os

mypath="/ug/ug2k18/cse/sai.tanmay/rand/ssd_scratch/cvit/starc52/VoxCeleb2/test_relocated/data/output_frames/"
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

list_of_names = [i[:-4] for i in onlyfiles]
cropped_path="/ug/ug2k18/cse/sai.tanmay/rand/ssd_scratch/cvit/starc52/VoxCeleb2/test_relocated/data/cropped_frames/"
output_path="/ug/ug2k18/cse/sai.tanmay/rand/ssd_scratch/cvit/starc52/VoxCeleb2/test_relocated/data/output_frames/"
audios_path="/ug/ug2k18/cse/sai.tanmay/rand/ssd_scratch/cvit/starc52/VoxCeleb2/test_relocated/data/audios/"
direct_output_path="/ug/ug2k18/cse/sai.tanmay/rand/ssd_scratch/cvit/starc52/VoxCeleb2/test_relocated/data/direct_output_frames/"

for i in list_of_names:
    f = open(cropped_path+i+".jpg")
    f1 = open(output_path+i+".jpg")
    f2 = open(audios_path+i+".wav")
    f3 = open(direct_output_path+i+".jpg")

    record = audImag(imgtitle=i+".jpg"), input_image.save(i+".jpg", File(f.read())), direct_output_image.save(i+".jpg", File(f3.read())), output_image.save(i+".jpg", File(f1.read())), songfile.save(i+".wav", File(f2.read()))
    record.save()
    f.close()
    f1.close()
    f2.close()
    f3.close()
