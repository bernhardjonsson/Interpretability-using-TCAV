# Interpretability-using-TCAV

## References

This repository uses code from the original [tensorflow/tcav](https://github.com/tensorflow/tcav)

## Downloading data

The data that were used are from [ImageNet](https://www.image-net.org/) but limited Imagenet dataset, which was used in these experiments,
can be downloaded from there [kaggle challenge](https://www.kaggle.com/competitions/imagenet-object-localization-challenge/data).

The random generation of folders is generated using the above dataset but the *random_gen.py* extracts random images from that folder.

I single class can also be downloaded by using following link *https://image-net.org/data/winter21_whole/wnid.tar* where the wnid of desired class can be found in the [LOC_synset_mapping.txt](https://www.kaggle.com/competitions/imagenet-object-localization-challenge/data?select=LOC_synset_mapping.txt)


## Running experiments

An example of the suit and fire engine experiments can be seen in there respective python files. These experiments used 200 items per folder and 25 random folders, due to unavailable computational resource the desired 500 random folder was unreacable.

A small demo experiment with explanations can be found in *TCAV_notebook.ipynb*

## Requirements
Following packages are required:

- tensorflow
- tcav
- numpy
- Pillow
- matplotlib
- scikit-learn
- scipy

A virtual environment can be set up using the requirements.txt.
If it is desired to run the code on a windows operating system, it recomended by tensorflow to set it up on windows subsystem. Therfore, a seperate requirements file for that type of setup is provided. The virtual environment on the subsystem was set up using a conda and python==3.9.15



