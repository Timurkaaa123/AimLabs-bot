import torch
from ultralytics import YOLO
import config.config as config

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

model = YOLO(f'models/{config.MODEL}/model.pt').to(device)