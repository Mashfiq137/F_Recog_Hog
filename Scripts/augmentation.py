from tensorflow.keras.preprocessing.image import ImageDataGenerator
from matplotlib.pyplot import imread, subplots,show
import numpy as np
import os
from PIL import Image
from skimage import io



import numpy as np
import keras,glob,os
import cv2
from keras.preprocessing.image import ImageDataGenerator, array_to_img,img_to_array, load_img

img_path = 'F:\\faces94\\dataset'
outpath = 'F:\\faces94\\Dataset_Aug\\'


filenames = glob.glob(img_path + "/**/*.jpg",recursive=True)


for img in filenames:

    if "DS_Store" in img: continue
    src_fname, ext = os.path.splitext(img)

    datagen = ImageDataGenerator(
            rotation_range = 45,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='reflect')


    img = load_img(img)

    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    img_name = src_fname.split('/')[-1]
    new_dir = os.path.join(outpath, src_fname.split('/')[-1].rsplit('-', 1)[0])
    #if not os.path.lexists(new_dir):
    #    os.mkdir(new_dir)
    #save_fname = os.path.join(new_dir, os.path.basename(img_name))
    save_fname = new_dir

    i = 0
    for batch in datagen.flow(x, batch_size=1, save_to_dir = save_fname,save_prefix = img_name, save_format='jpg'):
        i+=1
        if i>10:
            break
