# facelock
## About This Project  
Facelock is a plug-and-play facial recognition package for Python, designed for easy integration into your applications. It leverages powerful facial recognition models from [`Insightface`](https://github.com/deepinsight/insightface) to identify and compare facial features against saved reference images. The package uses OpenCV to access your webcam, enabling real-time facial authentication with minimal setup.

*Note:* this package upon import, downloads an Insightface model onto your desktop. If you do not wish to use these models, then look for other alternatives.

## Build Requirements
Ensure you have Python 3.8 or greater installed on your system along with an udpated version of pip. This model downloads the necessary python packages that are required including onnxruntime, insightface and opencv-python, but ensure that they are the most updated versions. If you already have an older version of any of these packages, installing this package may not update them. If facelock doesn't work, you should look to first upgrade the aforementioned packages to ensure they work with eachother. 

## Download
To download this package, use the following instructions:
  ```sh
  pip install facelock
  ```
If this does not work, then simply:
  ```sh
  pip install git+https://github.com/Ranuja01/facelock.git
  ```
## Example Usage
To use the module, simply import facelock as seen below:
```python
import facelock
```
Remember that this package is only functional assuming you have access to a webcam. This package currently returns only a boolean regarding whether or not the face seen by the webcam matches the face image that is stored. An example usage can be seen below:
```python
import facelock

img_path = "path_to_image.jpg"
is_match = facelock.get_authentication(img_path)

if is_match:
    print("User recognized!")
else:
    print("Unauthorized user!")      

```
