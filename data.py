# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 11:18:07 2018

@author: plagl
"""

import os
import coco
import json
import tensorflow as tf

class Data:
    def __init__(self, annotation_dir, image_dir):
        """
        Modified version of the COCO API.
        Constructor of Microsoft COCO helper class for reading and visualizing annotations.
        :param annotation_file (str): location of annotation file
        :param image_folder (str): location to the folder that hosts images.
        :return:
        """
        
        self.ann_dir = annotation_dir
        self.img_dir = image_dir
        
        # load dataset
        os.chdir( self.ann_dir )
        retval = os.getcwd()
        print("Directory changed successfully:", retval)
        self.API = coco.COCO("instances_train2017.json")
        
        
    def get_annotations(self, crowds=0):
        ann_ids = self.API.getAnnIds(imgIds=[], catIds=[], areaRng=[], iscrowd=crowds)
        anns = self.API.loadAnns(ann_ids)
        return anns
    
    
    def get_info(self, anns):
        img_ids = [a.get('image_id') for a in anns]
        info = self.API.loadImgs(img_ids)
        return info
    
    
    def load_labels(self, anns):
        labels = dict()
        for a in anns:
            labels[a.get('image_id')] = a.get('category_id')
            
        return labels
        
        
        
    def load_images(self, info):
        # loads all images - WIP    
        images = dict()
        os.chdir( self.img_dir )
        
        for i in info:
            images[i.get('id')] = tf.image.decode_jpeg(i.get('file_name'), channels=1)
                
        return images
    
    
    def convert_labels(self, labels):
        apple = 53
        banana = 52
        broccoli = 54
        
        (other, apples, bananas, broccolis) = (0,1,2,3)
        counts = [0,0,0,0]
        
        for key, value in labels.items():
            if value == apple:
                labels[key] = apples
                counts[apples] += 1
            elif value == banana:
                labels[key] = bananas
                counts[bananas] += 1
            elif value == broccoli:
                labels[key] = broccolis
                counts[broccolis] += 1
            else:
                labels[key] = other
                counts[other] += 1
                
        return labels, counts
            
        
# Create some variables.
ann_path = "D:\\cocoapi\\annotations\\"
img_path = "D:\\cocoapi\\images\\"
data = Data(ann_path, img_path)
anns = data.get_annotations()
info = data.get_info(anns)

lbl = data.load_labels(anns)
# img = data.load_images(info)
classes, counts = data.convert_labels(lbl)

# Save cats to json
with open('classes.json', 'w') as fp:
    json.dump(classes, fp)
            
            
            
            
            
            
            