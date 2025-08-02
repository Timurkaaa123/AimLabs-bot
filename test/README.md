# TESTING THE MODEL v1.0.0

The test checks the correctness of frame capture from the game window, the operation of the computer vision model and the visualization of overlays on frames.

## MODEL SETTINGS:
```python
# OBS Virtual Cam
FRAME_WIDTH = 420
FRAME_HEIGHT = 240


# Visualisation config
VISUALISATION = True

ALL_DETECTION_TARGETS_OVERLAY = True
CURRENT_TARGET_OVERLAY = True
FPS_OVERLAY = True

# Visualisation colors. Format - BGR (Blue, Green, Red)
FPS_COLOR = (0, 255, 0)
CURRENT_TARGET_COLOR = (0, 0, 255)

# Model version
MODEL = "1.0.0"


# AIMing settings
ACCURACY = 10.00 #The value defines the permissible deviation from the target center. Default: 0.00
```


## AimLabs:
**SENSITIVITY:** 1.00
**SCREEN MODE:** FULL SCREEN IN WINDOW
**SCREEN RESOLUTION:** 1280x720
**GRAPHICS QUALITY:** THE FASTEST

## OBS:
**OUTPUT RESOLUTION:** 424x240