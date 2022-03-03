import json
import cv2 as cv
import numpy as np 
import pandas as pd
from skimage import io
from scipy.cluster.vq import kmeans
import matplotlib.image as img
import binascii
import requests
import shutil 
from os import listdir
from os.path import isfile, join
import os
import pathlib

current_path = pathlib.Path(__file__).parent.resolve()
before_path =  pathlib.Path(current_path).parent.resolve() 

unknown_favicons_path = os.path.join(before_path ,"unknownFavicons") #'/'.join(dirarr)

print("unknown favicons path - "+unknown_favicons_path)

json_data_path = 'dominentdata.json'


def load_json_data():
  with open(json_data_path) as json_file:
      data = json.load(json_file)
    #   print("json hash"+data['hash'])
      return data

def load_favicons_from_dir():
    # dirarr.pop()
    # dirpath = '/'.join(dirarr)+'/favicons/'

    dirpath = os.path.join(before_path ,"favicons")
    print(dirpath)
    imagelist = sorted([f for f in listdir(dirpath) if isfile(join(dirpath, f))])
    listlen = len(imagelist)
    print("image count - "+str(listlen))
    image_data_dict = dict()
    for img in imagelist:
        # print(img)
        favicon_path = os.path.join(before_path ,"favicons",img)
        imgdata = get_image_data_from_path_cv(favicon_path)
        # print(imgdata[0])
        image_data_dict[img] = imgdata
    print("---images loading complete---")
    return image_data_dict

def get_image_data_from_path_cv(img_path):
  image = io.imread(img_path)
  image_data = cv.cvtColor(image, cv.COLOR_BGR2RGB)
  return image_data


def get_image_data_from_path_pil(img_path):
  image = io.imread(img_path)
  image_data = cv.cvtColor(image, cv.COLOR_BGR2RGB)
  return image_data


def getDominentColor(image_path):
    print(image_path)
    # image = get_image_data_from_path_cv(image_path) #img.imread(image_path)
    image = img.imread(image_path)
    # image = Image.open(image_path).convert('RGB')
    # print(image.shape)
    # image = asarray(image)
    # print(image[0][:3])

    r = []
    g = []
    b = []

    for row in image:
        for pixel in row:
            # A pixel contains RGB values
            r.append(pixel[0])
            g.append(pixel[1])
            b.append(pixel[2])

    df = pd.DataFrame({'red':r, 'green':g, 'blue':b})

    # print(df.head())

    cluster_centers, _ = kmeans(df[['red','green','blue']].values.astype(float), 1 ,seed=2)
    # print(cluster_centers[0])
    colour = binascii.hexlify(bytearray(int(c) for c in cluster_centers[0])).decode('ascii')
    # print('most frequent is %s (#%s)' % (cluster_centers[0], colour))

    nameimg = image_path.split('.')[-2]
    print(nameimg)
    return {"name":nameimg , "color":"#"+colour}



def get_favicon_from_google(url):
    
    urldomain = '_'.join(url.split("."))[8:]
    filepath = os.path.join(unknown_favicons_path ,urldomain+".ico")
    # filepath = unknown_favicons_path+"/"+urldomain+".ico"
    
    r = requests.get('https://www.google.com/s2/favicons?domain='+url, stream = True)

    if r.status_code == 200:
        
        r.raw.decode_content = True
        
        with open(filepath,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filepath , end='' , flush=True)
        return filepath

    else:
        print('Image Couldn\'t be retreived')
        return False


    # https://www.google.com/s2/favicons?domain='+url

    # unknow_favicon_path
    # image = io.imread(img_path)
    # image_data = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    # return image_data


def comp2imghistogramHISTCMP_BHATTACHARYYA(img1 , img2):
    img1_hist = cv.calcHist([img1], [0], None, [256], [0, 256])
    img2_hist = cv.calcHist([img2], [0], None, [256], [0, 256])
    

    img_hist_diff = cv.compareHist(img1_hist, img2_hist, cv.HISTCMP_BHATTACHARYYA)

    return round(img_hist_diff , 2)


def comp2imghistogramHISTCMP_CHISQR(img1 , img2):
    img1_hist = cv.calcHist([img1], [0], None, [256], [0, 256])
    img2_hist = cv.calcHist([img2], [0], None, [256], [0, 256])
    

    img_hist_diff = cv.compareHist(img1_hist, img2_hist, cv.HISTCMP_CHISQR)
    
    return round(img_hist_diff , 2)


def comp2imghistogramTM_CCOEFF_NORMED(img1 , img2):
    img1_hist = cv.calcHist([img1], [0], None, [256], [0, 256])
    img2_hist = cv.calcHist([img2], [0], None, [256], [0, 256])
    
    img_template_probability_match = cv.matchTemplate(img1_hist, img2_hist, cv.TM_CCOEFF_NORMED)[0][0]
    img_template_diff = 1 - img_template_probability_match
    # print(img_template_diff)
    return round(img_template_diff , 2)

def com2imageMSE(img1 , img2):
    y = 1000
    try:
      y = np.square(np.subtract(img1,img2)).mean()
      # print(y)
    except Exception as e:
      pass
    return round(y , 4)

def compareFavs(mode , threshold , img1 , img2):

  comptarget = 1000

  if mode == "HISTCMP_BHATTACHARYYA": 
    comptarget = comp2imghistogramHISTCMP_BHATTACHARYYA(img1 , img2)

  if mode == "TM_CCOEFF_NORMED": 
          comptarget = comp2imghistogramTM_CCOEFF_NORMED(img1 , img2)

  if mode == "MSE": 
          comptarget = com2imageMSE(img1 , img2)

  if mode == "HISTCMP_CHISQR":
          comptarget = comp2imghistogramHISTCMP_CHISQR(img1 , img2)

  # print(comptarget)
  if (comptarget<=threshold):
    return True
  else:
    return False

dominent_dataset = load_json_data()
image_data_dict = load_favicons_from_dir()

# print(image_data_dict)

# import matplotlib
# print('matplotlib: {}'.format(matplotlib.__version__))
# import scipy
# print('scipy: {}'.format(scipy.__version__))


# getDominentColor('/home/dealwithit/Documents/nemisis/favicons/zoom_us.ico')

