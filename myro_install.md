## Installing Myro and other prerequisites
Myro is very old and not well documented so here are some helpful instructions to aid in the installation process.

## Inital Setup
Ensure **python 2.7.14 32-bit or newer** is installed and set in the enviorment variable. 

## Installing Myro
 1. Download and extract this zip: [Download](http://www.betterbots.com/download/myro-install-2.9.5.zip)
 2. Download this custom install.bat file: [Download](https://gist.github.com/JoshuaA9088/1ca1a604adb084df65b32ab3e9a990f2/archive/3442e9a866c7e453541f9f51737842a18bb1f272.zip)
 3. Replace the install script included with the myro with the one you just downloaded
 4. Run install.bat **AS ADMINISTRATOR**
 5. Decline installing Python 2.4 and attempt to install the other modules, ensure you point all modules to install to **python 2.7** not python 2.4. If you get a missing MSVCR71.dll error, go back to step 4 but install python 2.4, again ensure you install all other modules to the **python 2.7** environment
 6. If you installed python 2.4 during the installation, it should be safe to uninstall after all the modules are installed
 7. Run ``pip install numpy matplotlib pywin32 pillow`` to install the other required modules.
 8. Test the install by opening a shell and attempting to import myro: ``from myro import *``
 9. Myro should return ``Myro version 2.9.5 is ready!`` Disregard the any Image TK warnings
 10. Upgrade myro with ``upgrade("myro")
 
## Troubleshooting
 - MSVCR71.dll missing error
   - Go reread step 5
  - Python 2.7 is not showing up in the module installer window
    - Ensure you have Python 2.7 **32-bit**
  
## FAQ
 - Why should I ignore the Image TK errors?
   - Because this module was written for python 2.4, it is not compatible with the change of syntax for TK in python 2.7. Myro doesn't really utilize many TK features and any crucial menus can be skipped with specific commands.
  - Why is MSVCR71.dll missing?
    - The missing DLL is included by Python 2.4 not 2.7 as an architectural change. Uninstalling python 2.4 after installing myro should not cause any issues.
  - Why is this so poorly updated and documented?
    - Myro was largely abandoned for standard python. The project moved to calico. If you would like to explore that here is the link: [Calico](http://wiki.roboteducation.org/Calico)
    
