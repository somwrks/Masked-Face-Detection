# Face Mask Detection

This project focuses on implementing a deep learning model for face mask detection using the VGG16 pre-trained model and transfer learning. The model is trained on a dataset of images with and without face masks.

## Overview

The project consists of the following components:

1. `paste.txt`: This file contains the main Python code for loading the dataset, preprocessing data, building and training the model, and performing real-time face mask detection.

## Dependencies

The project requires the following dependencies:

- NumPy
- Pandas
- OpenCV
- Keras
- scikit-learn
- TensorFlow (for Keras)

## Usage

1. Ensure all dependencies are installed.
2. Run the `paste.txt` file in a Python environment.

## Code Structure

The key components of the code include:

- Loading and preprocessing the dataset
- Building the VGG16 model and adding a custom dense layer
- Transfer learning by freezing the pre-trained layers
- Training the model on the dataset
- Real-time face mask detection using OpenCV

## Folder Structure

- `train`: Contains the training dataset with two folders: `with_mask` and `without_mask`.

## How to Contribute

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to create issues or pull requests.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute the code as per the terms of the license.

![image](https://github.com/somwrks/Masked-Face-Detection/assets/85481905/35cbe90d-34bf-4718-9890-ae0717a07e84)

![image](https://github.com/somwrks/Masked-Face-Detection/assets/85481905/62de7f6e-5217-4c52-b9fd-4363567ae737)
