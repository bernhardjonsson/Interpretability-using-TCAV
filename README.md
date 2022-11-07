# Interpretability-using-TCAV

## Downloading data

For downloading data run:

``` bash
python download_and_make_datasets.py --source_dir=YOUR_FOLDER --number_of_images_per_folder=50 --number_of_random_folders=3
```
If different classes and concepts are desired open "download_and_make_datasets.py" and change the "imagenet_classes" and "broden_concepts"
found at line number 49 and 50.
