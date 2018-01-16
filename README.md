## Robot Tracking

Using OpenCV2 and Numpy to track a robot. Specifically been used and tested with the Kaicong SIP 1602 Camera.

## Getting Started

Clone Repo

## Prerequisites
- Ensure **Python 2.7** is set in the environment variables of windows
- Python 2.7 (Used for image processing)
  - OpenCV v3.2
  - Numpy Latest
  - PySerial Latest through PIP
  - Pillow Latest
- Python 2.4 (Used for connecting to robot)
  - PySerial Latest for Python 2.4
  - Myro v2.99 or v2.95

## Running With Robot
Before running the image processing script (findRobot.py) the pipeline server for Python 2.4 (listen.py) must be started.
If you did not install Python 2.4 to the default directory, change the .bat file accordingly:

```
C:\Python24\python C:\WHERE YOU SAVED IT\KaiVid\listen.py
```

TO

```
C:\WHEREVER PYTHON 2.4 IS INSTALLED C:\WHERE YOU SAVED IT\KaiVid\listen.py
```

Listen.py will connect to your scribbler robot. Edit listen.py and change whatever COM port listed to your Robot's Port.

Run listen.bat

Call KaiVid/findRobot.py in CMD passing it the IP of the camera

```
python /WHERE YOU SAVED IT/KaiVid/findRobot.py #.#.#.#
```

## Running without Robot
None of the Python 2.4 environment is needed without the robot.
Edit /KaiVid/findRobot.py
Comment out the following line:

```
s.connect((HOST, PORT))
```

To

```
# s.connect((HOST, PORT))
```

Call KaiVid/findRobot.py in CMD passing it the IP of the camera

```
python /WHERE YOU SAVED IT/KaiVid/findRobot.py #.#.#.#
```
This should open 3 Windows showing the alternate chassis, board, and original images.

![alt text](https://raw.githubusercontent.com/JoshuaA9088/robotTracking/master/images/Robot Picked.PNG)

## Changing Thresholds
To change the threshold to identify different colors edit the findRobot.py script

Scroll down to:

```
redUpper = np.array([100, 150, 255], dtype=np.uint8) #Thresholds for chassis ID
redLower = np.array([0, 0, 100], dtype=np.uint8) #Thresholds for chassis ID

greenUpper = np.array([255, 50, 100], dtype=np.uint8) #Thresholds for board ID
greenLower = np.array([50, 0, 0], dtype=np.uint8) #Thresholds for board ID
```

Red thresholds are for the chassis of the robot, green for the blue strip.

Remember these values are in **BGR** NOT **RGB**


## Authors

* **Joshua Arulsamy**

## Acknowledgments

* **Roby Velez**
