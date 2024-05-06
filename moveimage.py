import os
import shutil

train_dir = 'train'

if not os.path.exists(train_dir):
    print(f"The directory '{train_dir}' does not exist.")
    exit()

with_mask_dir = os.path.join(train_dir, 'with_mask')
if not os.path.exists(with_mask_dir):
    os.makedirs(with_mask_dir)

for filename in os.listdir(train_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff')):
        if 'with-mask' in filename:
            shutil.move(os.path.join(train_dir, filename), with_mask_dir)
    else:
        pass

print(f"Moved images with 'with-mask' to '{with_mask_dir}'")