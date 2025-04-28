# facelock
## About This Project  
Facelock is a plug-and-play facial recognition package for Python, designed for easy integration into your applications. It leverages powerful facial recognition models from [`Insightface`](https://github.com/deepinsight/insightface) to identify and compare facial features against saved reference images. The package uses OpenCV to access your webcam, enabling real-time facial authentication with minimal setup.

**Note:** this package upon import, downloads an Insightface model onto your desktop. If you do not wish to use these models, then look for other alternatives.

## Build Requirements
Ensure you have Python 3.8 or greater installed on your system along with an udpated version of pip. This model downloads the necessary python packages that are required including onnxruntime, insightface and opencv-python-headless, but ensure that they are the most updated versions. **Note:** If you already have opencv-python installed, this may conflict with opencv-python-headless. In order to use this package, uninstall opencv-python. If you already have an older version of any of these packages, installing this package may not update them. If facelock doesn't work, you should look to first upgrade the aforementioned packages to ensure they work with eachother. 

## Download
**This package currently requires an Anaconda Python distribution due to internal dependencies that install and use ONNX.**

**InsightFace, one of the core dependencies, requires a C++ compiler to operate properly.
Please make sure you have a C++ compiler installed on your system before proceeding.:**
### Windows  
- Download and install **Microsoft Visual C++ Build Tools 2022** or later from:  
  [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)  
- Ensure you select the **C++ CMake tools for Windows** and **MSVC compiler** during installation.
- To verify you have correctly installed the C++ compiler run this in the Developer Command Prompt (not the regular command prompt):
  ```sh
  cl
  ```
- *Note* that simply installing MSVC build tools may not initialize your system properly. You may have to set environment
  variables or update your path with the cl.exe compiler.
### Linux  
- Install the necessary C++ compiler and build tools:
  - For Ubuntu: 
  ```sh
  sudo apt update && sudo apt install build-essential
  ```
  - For Fedora:
  ```sh
  sudo dnf install gcc-c++ make
  ```
- To verify you have correctly installed the C++ compiler run this in a terminal:
  ```sh
  g++ --version 
  ```
### For MacOS
- Install Apple's command-line developer tools (includes clang for C++):
  
  ```sh
  xcode-select --install
  ```
- To verify you have correctly installed the C++ compiler run this in a terminal:
  ```sh
  g++ --version 
  ```
  
**To download this package, use the following instructions:**
  ```sh
  pip install facelock
  ```
If this does not work, then simply:
  ```sh
  pip install git+https://github.com/Ranuja01/facelock.git
  ```
## Example Usage
To use the module, simply import facelock as seen below. Keep in mind that the first usage should generally take a few more seconds as the required models are being stored:
```python
import facelock
```
*Note:* This package requires access to a webcam to function properly. Currently, it returns a simple boolean indicating whether the face detected by the webcam matches a stored reference image. The facial recognition process takes approximately 2.5 seconds (slightly longer on first use) to complete. Below is an example demonstrating how to use the package:
```python
import facelock

img_path = "path_to_image.jpg"
is_match = facelock.get_authentication(img_path)

if is_match:
    print("User verified!")
else:
    print("Unauthorized user!")      
```
