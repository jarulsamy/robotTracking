**Table of Contents**
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Result](#result)
- [Changing Thresholds](#changing-thresholds)

## Getting Started

Clone Repo (No official release built yet)

## Prerequisites
- Python 2.7 (Used for image processing)
  - Ensure **Python 2.7** is set in the environment variables of Windows
- OpenCV v3.2 or v2.4
- Numpy Latest
- Pillow Latest
- PySerial Latest

## Usage
  Call findRobot.py through CMD passing it the IP of the camera:

  ```
  python vidOnly.py IP_ADDRESS
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
