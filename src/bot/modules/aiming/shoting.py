import ctypes
from ctypes import wintypes
import config.config as config

mouse = ctypes.WinDLL('src/bot/dll/mouse.dll')

mouse.Move.argtypes = [ctypes.c_int, ctypes.c_int]
mouse.Move.restype = None

mouse.LeftClick.argtypes = None
mouse.LeftClick.restype = None


def movement(target, frame):
	# Center
	height, width = frame.shape[:2]
	center_x = width // 2
	center_y = height // 2

	# Position
	target_x = target[0][0]
	target_y = target[0][1]

	# Mouse Movement
	x = (center_x - target_x) 
	y = (center_y - target_y) 


	mouse.Move(-x, -y)

def shot(target, frame):
	# Points
	target_x = target[0][0]
	target_y = target[0][1]

	# Center
	height, width = frame.shape[:2]
	center_x = width // 2
	center_y = height // 2
	center = (center_x, center_y)


	if abs(target_x - center_x) < config.ACCURACY and abs(target_y - center_y) < config.ACCURACY:
		mouse.LeftClick()
	else:
		movement(target, frame)
