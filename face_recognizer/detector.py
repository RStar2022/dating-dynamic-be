import cv2
import face_recognition
import numpy as np
from flask import Flask, request, jsonify

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

class FaceDetection():
      def face_detection(image): 
            nparr = np.frombuffer(image, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            #Faces detection
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

            response_data = []

            for (x,y,w,h) in faces :
                  #Draw box
                  cv2.rectangle(image, (x,y), (x + w, y + h), (0, 255, 0), 2)
                  
                  #Calculate confidence score (set as 1.0)
                  confidence = 1.0

                  cv2.putText(image, f"Confidence: {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                  response_data.append({
                        'x':x,
                        'y':y,
                        'width':w,
                        'height':h,
                        'confidence':confidence
                  })

                  return jsonify(response_data)
            return "Image not found", 404

    
