import numpy as np
import cv2 as cv

#classificador pré-treinado do opencv:
face_classifier = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
 
#
cap = cv.VideoCapture(0) #camera do notebook
if not cap.isOpened():
    print("vixe, não foi possível abrir a câmera")
    exit()

while True:
    # capturando frame por frame
    ret, frame = cap.read() #essa função retorna um valor booleano (ret) e frame é imagem capturada em rgb
 
    # ret é um valor booleano q pode ser verdadeiro ou falso, se for falso (ou seja, n conseguiu capturar o frame):
    if not ret:
        print("af, não consegui capturar o frame")
        break
    # deixando a imagem em preto e branco
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #iremos guardar a imagem convertida na variavel gray
    


    #detectando o rosto:
    faces = face_classifier.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )

    # desenhando a caixa ao redor do rosto
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #mostrando a imagem na tela
    cv.imshow('Teste', frame) #podemos colocar frame ou gray, depende do que queremos mostrar ao usuário
    if cv.waitKey(1) == ord('q'): #interrope o loop so se apertar em q
        break

print(f"Eba! Detectamos {len(faces)} face(s)") #só pra confirmar se a detecção tá dando certo

# finalizando
cap.release() #libera a camêra
cv.destroyAllWindows() 