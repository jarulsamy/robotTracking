## Robot Tracking

Using OpenCV2 and Numpy to track a robot. Specifically been used and tested with the Kaicong SIP 1602 Camera.

**Table of Contents**

- [Getting Started](#)
- [Prerequisites](#)
- [How we Connect to the robot](#)
- [Running With Robot](#)
- [Running without Robot](#)
- [Result](#)
- [Changing Thresholds](#)
- [Authors](#)
- [Acknowledgments](#)


## Getting Started

Clone Repo

## Prerequisites
- Python 2.7 (Used for image processing)
  - Ensure **Python 2.7** is set in the environment variables of Windows **NOT** Python 2.4
  - OpenCV v3.2 or v2.4
  - Numpy Latest
  - PySerial Latest through PIP
  - Pillow Latest
- Python 2.4 (Used for connecting to robot)
  - PySerial Latest for Python 2.4
  - Image TK Latest for Python 2.4
  - Myro v2.99 or v2.95 (Pain to Install, Will have Image TK error, Ignore)

## How we Connect to the robot
Due to the age of Myro, it is only compatible with Python 2.4. Anything newer moved to Calico which at the moment does not support OpenCV. Listen.py connects to the robot in a Python 2.4 instance, then creates a listening server on port 10000.
The findRobot.py script, sends instructions to this server and moves the robot. Running without the robot is detailed down below.
[Running without Robot](#)

## Running With Robot
Before running the image processing script (findRobot.py) the pipeline server for Python 2.4 (listen.py) must be started.
If you did not install Python 2.4 to the default directory, change the .bat file accordingly:

```
C:\Python24\python C:\WHERE YOU SAVED IT\KaiVid\listen.py
```

TO

```
C:\WHEREVER PYTHON 2.4 IS INSTALLED\python C:\WHERE YOU SAVED IT\KaiVid\listen.py
```

Listen.py will connect to your scribbler robot. Edit listen.py and change whatever COM port listed to your Robot's Port.

Run listen.bat

Call KaiVid/findRobot.py in CMD passing it the IP of the camera

```
python /WHERE YOU SAVED IT/KaiVid/findRobot.py #.#.#.#
```
This should be done with **Python 2.7** if not in your environment variable

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

## Result
This should open 3 Windows showing the alternate chassis, board, and original images.

**Robot Picked**
<img src="https://user-images.githubusercontent.com/14321139/34995801-d096836a-fa94-11e7-9c0d-7db769829056.PNG" alt="Robot Picked" width="320" height="240">

**Front Picked**
<img src="https://user-images.githubusercontent.com/14321139/34995798-cff908e2-fa94-11e7-96e2-6e31c177178c.PNG" alt="Front Picked" width="320" height="240">

**Centroids**
<img src="https://user-images.githubusercontent.com/14321139/34995799-d02e19f6-fa94-11e7-850f-02060456b2b1.PNG" alt="Centroids" width="320" height="240">

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
* **Cameron Whiting**
