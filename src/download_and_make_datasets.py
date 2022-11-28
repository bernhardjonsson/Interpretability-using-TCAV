"""
Copyright 2018 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
""" Downloads models and datasets for imagenet

    Content downloaded:
        - Full Broden dataset(http://netdissect.csail.mit.edu/)
        - Inception 5h model(https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/inception5h.py)
        - Mobilenet V2 model(https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md)

    Functionality:
        - Downloads open source models(Inception and Mobilenet)
        - Extracts color concepts from the Broden dataset(red-c, yellow-c, green-c, blue-c)
        - Structures the data in a format that can be readily used by TCAV

    Example usage:

    python download_and_make_datasets.py --source_dir=YOUR_FOLDER --number_of_images_per_folder=50
"""
import subprocess
import os
import argparse
from tensorflow.io import gfile
import imagenet_and_broden_fetcher as fetcher
from find_img_color import *

def make_concepts_targets_and_randoms(source_dir, number_of_images_per_folder):
    # Run script to download data to source_dir
    if not gfile.exists(source_dir):
        gfile.makedirs(source_dir)
    if not gfile.exists(os.path.join(source_dir,'broden1_224/')) or not gfile.exists(os.path.join(source_dir,'inception5h')):
        subprocess.call(['bash' , 'FetchDataAndModels.sh', source_dir])
        #Rename images for color concept
        rename_img(source_dir)


    # Determine concepts that we will fetch
    broden_concepts = ['red-c', 'yellow-c', 'blue-c', 'green-c']

    # Make concepts from broden - color
    for concept in broden_concepts:
        fetcher.download_color_to_working_folder(broden_path=os.path.join(source_dir, 'broden1_224'),
                                                   saving_path=source_dir,
                                                   color_name=concept,
                                                   number_of_images=number_of_images_per_folder)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create examples and concepts folders.')
    parser.add_argument('--source_dir', type=str,
                        help='Name for the directory where we will create the data.')
    parser.add_argument('--number_of_images_per_folder', type=int,
                        help='Number of images to be included in each folder')

    args = parser.parse_args()
    # create folder if it doesn't exist
    if not gfile.exists(args.source_dir):
        gfile.makedirs(os.path.join(args.source_dir))
        print("Created source directory at " + args.source_dir)
    # Make data
    make_concepts_targets_and_randoms(args.source_dir, args.number_of_images_per_folder)
    print("Successfully created data at " + args.source_dir)

