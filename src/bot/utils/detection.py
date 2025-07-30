import torch 
import numpy
from .model import model


def detect(frame):
	with torch.no_grad():
		results = model(frame, verbose=False)


	detections = results[0]

	boxes = detections.boxes.xyxy.cpu().numpy()

	scores = detections.boxes.conf.cpu().numpy()

	classes = detections.boxes.cls.cpu().numpy()


	threshold = 0.5
	filtered_boxes = boxes[scores > threshold]
	filtered_scores = scores[scores > threshold]
	filtered_classes = classes[scores > threshold]

	for box, score, cls in zip(filtered_boxes, filtered_scores, filtered_classes):
	    x1, y1, x2, y2 = box
	    print(
		    f"Координаты: ({x1:.1f}, {y1:.1f}, {x2:.1f}, {y2:.1f}), "
		    f"класс: {int(cls)}, уверенность: {score:.2f}"
		)

	return results[0]
