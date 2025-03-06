import cv2

def blur_faces(image_path, output_path):

    image = cv2.imread(image_path)
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=2, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        blurred_face = cv2.GaussianBlur(face, (51, 51), 30)  
        image[y:y+h, x:x+w] = blurred_face
    
    cv2.imwrite(output_path, image)
    
    print(f"Image sauvegardée sous : {output_path}")

input = input("Enter the image path : ")
blur_faces(input, 'output.jpg')
