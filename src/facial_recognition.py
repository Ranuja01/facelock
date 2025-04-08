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

