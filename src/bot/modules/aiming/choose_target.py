import numpy

def choose_target(targets, frame):
	# Find center
	height, width = frame.shape[:2]
	center_x = width // 2
	center_y = height // 2


	# Coordinats
	boxes = targets.boxes.xyxy.cpu().numpy() 

	# Scores
	scores = targets.boxes.conf.cpu().numpy()

	# Filtration
	threshold = 0.5
	filtered_boxes = boxes[scores > threshold]
	filtered_scores = scores[scores > threshold]

	# Chose target
	min_diff = float('inf')
	points = []

	for box, score in zip(filtered_boxes, filtered_scores):
		x1, y1, x2, y2 = box
		x = int( (x1 + x2) // 2 )
		y = int( (y1 + y2) // 2 )

		diff = abs(x - center_x) + abs(y - center_y)

		if diff <= min_diff:
			min_diff = diff
			points = [(x, y), (x1, y1), (x2, y2)]

	return points