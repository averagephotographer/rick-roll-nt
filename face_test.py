from PIL import Image
import face_recognition

# image = face_recognition.load_image_file("C:\\Users\cdtv1\\Desktop\\photos\chris\chris_web\DSC_6898.jpg")
image = face_recognition.load_image_file("C:\\Users\cdtv1\\Desktop\\photos\presidents.jpg")
# face_locations = face_recognition.face_locations(image)
face_locations = face_recognition.face_locations(image, model="cnn")

print(f"I found {len(face_locations)} face(s) in this photograph")

for face_location in face_locations:
    top, right, bottom, left = face_location

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
