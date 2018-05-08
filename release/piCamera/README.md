## Raspberry Pi Camera Running With Robot  

**Table of Contents**
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Result](#result)
- [Changing Thresholds](#changing-thresholds)

## Getting Started

Clone Repo (No official release built yet)

## Prerequisites
- Raspberry Pi and Camera
- Python 2.7
- OpenCV v3.2
- Numpy
- PySerial V2.2 (Anything newer is not compatible with myro, should be included in myro download)
- Myro v2.99 or v2.95: [Download](http://www.betterbots.com/download/myro-install-2.9.5.zip)

## Raspberry Pi Setup
  - Ensure that the Raspberry Pi is completely up to date with:
  ```
  sudo apt-get update  
  sudo apt-get upgrade
  ```
  - Run ``` sudo raspi-config``` and enable the camera
  - Python3 should be preinstalled with Raspbian, otherwise install it
  - Install the following Packages
    - picamera
    - socketserver
    - http  
  - This script must be running on the raspberry pi at all times to connect to the camera:  [Download](https://gist.github.com/JoshuaA9088/a47b948ce61361230d387555eec84b57/archive/daa53c14bc95cb01e9cac1056fcfeab9c13dbf49.zip)

## Changing Camera Properties
**TODO**

## Multithreading
  To keep the robot from slowing down the image processing, the script is multithreaded. The class ``moveThread`` contains all orientation and movement code.

## Usage
  Call findRobot.py through CMD passing it the IP of the Pi including port and the COM port of the robot. In this case the camera port should always be 8000 due to the custom script running on the Pi.

  ```
  python findRobot.py IP_ADDRESS:8000 COMX
  ```  

## Running without robot
  To run the script without a robot, pass ``onlyVision`` instead of the com port

  ```
  python findRobot.py IP_ADDRESS:8000 onlyVision
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
  To change the threshold to identify different colors edit the findRobot.py script scroll down to:

  ```
  redUpper = np.array([b, g, r], dtype=np.uint8) #Thresholds for chassis ID
  redLower = np.array([b, g, r], dtype=np.uint8) #Thresholds for chassis ID

  greenUpper = np.array([b, g, r], dtype=np.uint8) #Thresholds for board ID
  greenLower = np.array([b, g, r], dtype=np.uint8) #Thresholds for board ID
  ```

  Red thresholds are for the chassis of the robot, green for the blue strip.

  Remember these values are in **BGR** NOT **RGB**
