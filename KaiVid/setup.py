#Setup.py
from distutils.core import setup
import py2exe

def __unicode__(self):
   return unicode(self.some_field) or u''


setup(
    console =['findRobot.py'],
    options ={
        'py2exe' : {
            'packages' : ['base.KaicongInput','socket','sys','numpy','cv2','math','time']
        }
    }
)
