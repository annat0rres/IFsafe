import cv2
import matplotlib.pyplot as plt


imagePath = 'Frank Ocean.jpeg'

img = cv2.imread(imagePath)
plt.imshow(img) 

img.shape
(4000, 2667, 3)

#convertendo a imagem para cores na escala de cinza, visto q é mais fácil

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_image.shape
(4000, 2667)

#carregar o classificador - pré treinado integrado ao OpenCv

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

#executando a deteccção de face na imagem em escala de cinza

face = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize = (40, 40)
)

#caixa delimitadora
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)

#exibindo imagem

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#imprimindo caixinha ao redor do rosto
plt.figure(figsize = (20, 10))
plt.imshow(img_rgb)
plt.axis('off')

