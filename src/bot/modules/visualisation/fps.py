import cv2
import time
import config.config as config

def add_FPS(frame, prev_time, curr_time):
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time else 0
    prev_time = curr_time

    cv2.putText(frame, f'FPS: {fps:.2f}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, config.FPS_COLOR, 2)

    return frame, fps
