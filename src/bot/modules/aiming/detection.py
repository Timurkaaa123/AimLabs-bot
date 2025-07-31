import torch 
import numpy
from ..model import model


def detect(frame):
	with torch.no_grad():
		results = model(frame, verbose=False)

	detections = results[0]


	return results[0]
