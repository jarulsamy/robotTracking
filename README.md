# Robot Tracking

Using OpenCV2 and Numpy to track a robot. Specifically been used and tested with the Kaicong SIP 1602 Camera.

## Getting Started

Clone Repo

## Prerequisites
- Python 2.7 (Used for image processing)
  - OpenCV v3.2
  - Numpy Latest
  - Pyserial
- Python 2.4 (Used for connecting to robot)
  - Pyserial
  - Myro v2.99 or v2.95

## Running
Before running the image processing script (findRobot.py) the pipeline server for Python 2.4 (listen.py) must be started.
If you did not install Python 2.4 to the default directory, change the .bat file accordingly:

```
C:\Python24\python C:\WHERE YOU SAVED IT\KaiVid\listen.py
```

TO

```
C:\WHEREVER PYTHON 2.4 IS INSTALLED C:\WHERE YOU SAVED IT\KaiVid\listen.py
```


Run listen.bat

Call KaiVid/findRobot.py in cmd with
```
python /WHERE YOU SAVED IT/KaiVid/findRobot.py
```
Ensure **Python 2.7** is set in the environment variables of windows

## Authors

* **Joshua Arulsamy**

## Acknowledgments

* **Roby Velez**
