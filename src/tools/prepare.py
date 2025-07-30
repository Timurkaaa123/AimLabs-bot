from PIL import Image
import os
import shutil
from pathlib import Path
import argparse
from tqdm import tqdm

# Folder
FOLDER = "./dataset/"

# Config:
SIZE = (400, 800)
START_NUM = 1

# Percents
VAL_PERCENT = 20

# Resize
def resize_image(path, max_size=(400, 800)):
    with Image.open(path) as img:
        orig_width, orig_height = img.size
        
        scale_w = max_size[0] / orig_width
        scale_h = max_size[1] / orig_height
        
        scale = min(scale_w, scale_h)
        
        new_width = int(orig_width * scale)
        new_height = int(orig_height * scale)
        
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        resized_img.save(path)
        print(f"Resize: {path}")

def resize_images(folder_path, max_size=(400, 800)):
    folder = Path(folder_path)
    image_exts = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}
    for file_path in tqdm(folder.iterdir()):
        if file_path.is_file() and file_path.suffix.lower() in image_exts:
            print(file_path)
            resize_image(str(file_path), max_size)

# Rename
def rename(directory):
    files = os.listdir(directory)
    counter = START_NUM
    for filename in tqdm(files):
        if filename == 'classes.txt':
            continue 
        if 'dataset_' in filename:
                continue

        old_path = os.path.join(directory, filename)
        if os.path.isfile(old_path):
            _, ext = os.path.splitext(filename)
            old_name = filename[:-3]

            new_name = f'dataset_{counter}{ext}'
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)

            path = old_path[:-3] + 'txt'
            new_name = f'dataset_{counter}.txt'
            new_path = os.path.join(directory, new_name)
            os.rename(path, new_path)

            counter += 1



def organize_files(source_dir, percent):
    source_dir = Path(source_dir)

    dataset_dir = Path(source_dir)
    labels_train = dataset_dir / 'labels' / 'train'
    labels_val = dataset_dir / 'labels' / 'val'
    images_train = dataset_dir / 'images' / 'train'
    images_val = dataset_dir / 'images' / 'val'

    for p in tqdm([labels_train, labels_val, images_train, images_val, dataset_dir]):
        p.mkdir(parents=True, exist_ok=True)

    image_exts = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}

    for file in tqdm(source_dir.iterdir()):
        if file.is_file():
            if file.name == "classes.txt":
                continue
            elif file.suffix.lower() == '.txt':
                shutil.move(file, labels_train / file.name)
            elif file.suffix.lower() in image_exts:
                shutil.move(file, images_train / file.name)
            else:
                pass

    def move_percent_files(train_path, val_path, percent):
        files = sorted(train_path.iterdir(), key=lambda f: f.name, reverse=True)
        total = len(files)
        count_to_move = int(total * percent / 100)
        for f in tqdm(files[:count_to_move]):
            shutil.move(str(f), val_path / f.name)

    move_percent_files(labels_train, labels_val, percent)
    move_percent_files(images_train, images_val, percent)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--resize', action='store_true', help="resize files")
    parser.add_argument('--rename', action='store_true', help="rename files")
    parser.add_argument('--organize', action='store_true', help="organize files")

    args = parser.parse_args()

    if args.resize:
        resize_images(FOLDER, SIZE)
    elif args.rename:
        rename(FOLDER)
    elif args.organize:
        organize_files(FOLDER, VAL_PERCENT)
    else:
        print("Use \"--resize\", \"--rename\" or \"--organize\"")

    
