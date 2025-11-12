import cv2
import mediapipe as mpipe

# Crear el objeto que maneja vidios
# dónde el argumento de la función es
# ya sea el dispositivo a usar (cámara)
cap = cv2.VideoCapture(0)

# Obtener las carapterísticas del dispositov
# Frames per second
fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS: ", fps)
# Tamaño del video
fWidth = int(cap.get(3))
fHeight = int(cap.get(4))
tam = (fWidth, fHeight)
print("Tamaño: ", tam)

# Iniciar el modelo de detección de manos de MediaPipe

mp_hands = mpipe.solutions.hands  # Acceso al módulo de manos
hands = mp_hands.Hands(
    static_image_mode=False,  # Si se debe usar en imágenes estáticas o en video
    max_num_hands=2,          # Máximo número de manos a detectar
    min_detection_confidence=0.5,  # Umbral de confianza para la detección inicial
    min_tracking_confidence=0.5    # Umbral de confianza para el seguimiento
)
mp_drawing = mpipe.solutions.drawing_utils  # Herramienta para dibujar los resultados de MediaPipe

while True:
    # Leer el dispositivo de entrada
    ret, frame = cap.read()
    # Si ret es False, quiere decir que no se
    # obtuvo información alguna
    if ret == False:
        break  # Entonces, se rompe y no hace nada
    # AQUÍ SE PROCESA MEDIAPIPE PARA DETECCIÓN DE MANOS
    # Convertir la imagen a RGB (MediaPipe trabaja en este espacio de color)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesar la imagen con el modelo de MediaPipe
    results = hands.process(frame_rgb)

    # Si hubo detección
    #if results.multi_face_landmarks:
    if results.multi_hand_landmarks:
        #for face_landmarks in results.multi_face_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Dibujar un círculo amarillo en la punta del dedo índice (landmark 8)
            index_finger_tip = hand_landmarks.landmark[12]  # Landmark de la punta del dedo índice
            index_finger_tip2 = hand_landmarks.landmark[8]
            x = int(index_finger_tip.x * fWidth)  # Convertir coordenadas normalizadas a pixeles
            y = int(index_finger_tip.y * fHeight)
            
            x2 = int(index_finger_tip2.x * fWidth)  # Convertir coordenadas normalizadas a pixeles
            y2 = int(index_finger_tip2.y * fHeight)            

            # Dibujar el círculo en la imagen
            cv2.circle(frame, (x, y), radius=80, color=(120, 205, 55), thickness=-1)  # Círculo amarillo
            cv2.circle(frame, (x2, y2), radius=20, color=(220, 50, 200), thickness=-1)  # Círculo amarillo

    # Mostrar el video con las manos detectadas
    cv2.imshow("Detección de Manos", frame)

    #####################
    # Si se presiona una tecla, em este caso ESC
    # se sale del ciclo
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Una vez hecho todo, liberar a Willy
# El video
cap.release()
# El archivo guardado
#resultado.release()
# Cerrar todas las ventanas
cv2.destroyAllWindows()
