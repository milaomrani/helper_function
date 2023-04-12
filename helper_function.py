# How to read a folder of images and crop the images from middle and save two part in png ground truth and source in python

import os
import cv2

# path of images
img_path = "/content/drive/MyDrive/dataset/train"

bad_path = "/content/notGood_images"
src_path = "/content/source_images"

for filename in os.listdir(img_path):
  img = cv2.imread(os.path.join(img_path, filename))
  # crop the image from middle
  height, width, _ = img.shape
  bad_img = img[0:height, 0:width//2]
  src_img = img[0:height, width//2:width]
  # save the two parts
  cv2.imwrite(os.path.join(bad_path, "corr_"+filename), bad_img)
  cv2.imwrite(os.path.join(src_path, "src_"+filename), src_img)

# -----------------------------------------------------------------
# renaming the whole images
import os
import glob
import argparse
import random
parser = argparse.ArgumentParser(description="")
parser.add_argument('--src', type=str, required=True, help='Path to src images')
parser = parser.parse_args()

source_folder = parser.src

for filename in os.listdir(source_folder):
    if filename.endswith("_G_1.JPG"):
        print(filename)
        new_filename = filename.replace("_G_1.JPG", "_1.JPG")
        os.rename(os.path.join(source_folder, filename), os.path.join(source_folder, new_filename))
        print(new_filename)
