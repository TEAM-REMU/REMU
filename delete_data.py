import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "remu.settings")
import django
django.setup()
from director.models import *
from mv.models import *


production = Production.objects.all()
production.delete()

director = Director.objects.all()
director.delete()

mv = MusicVideo.objects.all()
mv.delete()

