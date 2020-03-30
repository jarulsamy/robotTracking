## Robot Tracking

Using OpenCV2 and Numpy to track a Scribbler 2 robot. A raspberry pi with a camera is used to locate and track the robot.
The ultimate objective of this script is to be able to click somewhere within a window and have the robot move to that location based on alternate color space tracking.

Table of Contents
=================

      * [Robot Tracking](#robot-tracking)
      * [Getting Started](#getting-started)
      * [Prerequisites](#prerequisites)
      * [Raspberry Pi Setup](#raspberry-pi-setup)
      * [Changing Camera Properties](#changing-camera-properties)
      * [Usage](#usage)
      * [Result](#result)
      * [Support](#support)

## Getting Started

Clone Repo (No official release built yet)

## Prerequisites

-   Raspberry Pi and Camera
-   Python 3.6+
-   OpenCV
-   Numpy
-   PySerial
-   Myro v3.0.0+ [Install Instructions](https://github.com/jarulsamy/robotTracking/blob/master/myro_install.md)

## Raspberry Pi Setup

-   Ensure that the Raspberry Pi is completely up to date with:
        sudo apt-get update
        sudo apt-get upgrade

-   Run ` sudo raspi-config` and enable the camera

-   Python3 should be preinstalled with Raspbian, otherwise install it:

        sudo apt install python3

-   Install the rest of the dependencies

        pip3 install picamera socketserver http

-   [This](PyLivecam/livecam.py) script must be running on the raspberry pi at all times to connect to the camera.

## Changing Camera Properties

**TODO** (This still needs to be implemented in the livecam level.)

## Usage

**TODO** (Include more information about multithreading implementation, and calibration/orientation keybinds.)

## Result

<!-- These images are going to definietly change! -->

  **Robot Picked**
  <img src="https://user-images.githubusercontent.com/14321139/34995801-d096836a-fa94-11e7-9c0d-7db769829056.PNG" alt="Robot Picked" width="320" height="240">

  **Front Picked**
  <img src="https://user-images.githubusercontent.com/14321139/34995798-cff908e2-fa94-11e7-96e2-6e31c177178c.PNG" alt="Front Picked" width="320" height="240">

  **Centroids**
  <img src="https://user-images.githubusercontent.com/14321139/34995799-d02e19f6-fa94-11e7-850f-02060456b2b1.PNG" alt="Centroids" width="320" height="240">

## Support

Reach out to me at one of the following places!

-   Email (Best) at joshua.gf.arul@gmail.com
-   Twitter at <a href="http://twitter.com/jarulsamy_" target="_blank">`@jarulsamy_`</a>

* * *
