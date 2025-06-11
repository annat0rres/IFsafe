#código para abrir a câmera 
import cv2

cap = cv2.VideoCapture (1) #para uma câmera IP - externa a máquina

#verifica se a câmera abriu corretamente 
if not cap.isOpened (): 
    print ("Error: Não conseguimos achar a câmera")
    exit ()
else:
    print("Deu certo! A vida é bela")


#loop de captura de telas 
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: não consegui ler o frame")
        break
    
    #processa a imagem 
    cv2.imshow('Galeria', frame)

    #sai do loop quando 'q' é pressionado
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()