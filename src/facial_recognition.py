"""
@author: Ranuja Pinnaduwage

This file is part of facelock, a plug-and-play facial recognition package in Python

Description:
This file implements the core logic of the package
  
Copyright (C) 2025 Ranuja Pinnaduwage  
Licensed under the MIT License.  

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
"""

from insightface.app import FaceAnalysis
import cv2
import numpy as np
from timeit import default_timer as timer

def initialize_face_model():
    app = FaceAnalysis(allowed_modules=['detection', 'recognition'])
    app.prepare(ctx_id=0, det_size=(640, 640))

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_authentication(path):
    
    app = FaceAnalysis(allowed_modules=['detection', 'recognition'])
    app.prepare(ctx_id=0, det_size=(640, 640))
    
    img1 = cv2.imread(path)
    faces1 = app.get(img1)
    stored_image_embedding = faces1[0].embedding
    
    # Open webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()
        
    t0 = timer()
    frame_count = 0
    similarity_total = 0
    
    while (timer() - t0) < 2.5:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        faces = app.get(frame)
        
        for face in faces:
            current_embedding = face.embedding
    
            similarity = cosine_similarity(stored_image_embedding, current_embedding)
            
            similarity_total += similarity
            frame_count += 1
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    
    # Typical threshold for matching
    if similarity_total/frame_count > 0.6:
        # Matches
        return True        
    return False

