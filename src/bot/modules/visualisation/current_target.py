import cv2
import config.config as config

def add_target(frame, target):
    height, width = frame.shape[:2]

    target = target[0]

    cv2.line(frame, (target[0], height), (target[0], 0), config.CURRENT_TARGET_COLOR)
    cv2.line(frame, (0, target[1]), (width, target[1]), config.CURRENT_TARGET_COLOR)
    
    return frame
