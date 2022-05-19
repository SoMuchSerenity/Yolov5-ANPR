## Yolov5 Automatic NUmber Plate Recognition project

The body of the project is copied from https://github.com/ultralytics/yolov5

It is intended to complete the task of recognizing Ukrainian car plates

Custom dataset formed from 2 sources: https://www.kaggle.com/datasets/pcmill/license-plates-on-vehicles and  https://www.kaggle.com/datasets/sachinpatel21/pothole-image-dataset

The first source contains the car plates mostly from Netherlands, in order to let the object detection algorithm capture the Ukrainian car plates, which should be similiar to the Netherlands ones. The second source

A Flask web app is made and allows user to load a batch pf images. The batch will then be processed to give the user the cropped plate images.

To-do list:
1. Apply OCR to extract the numbers and characters of the car plate.
2. Perfect the Flask app to show better interface. Display the original iamges, cropped images, and the extracted number plate contents in the web.
3. Replace OCR with more accurate techniques, such as custom CNN-LSTM model to identify the numbers and characters.
