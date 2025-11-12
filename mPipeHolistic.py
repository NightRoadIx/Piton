# Importar las bibliotecas necesarias
import cv2  # OpenCV para manejo de video e imágenes
import mediapipe as mp  # MediaPipe para modelos de visión por computadora
import time  # Para calcular FPS

# Acceso a herramientas de dibujo de MediaPipe
mp_drawing = mp.solutions.drawing_utils
# Acceso al modelo Holistic de MediaPipe (pose, manos, rostro)
mp_holistic = mp.solutions.holistic

# Inicializar la captura de video. Puede ser desde un archivo o una cámara
# cap = cv2.VideoCapture(r"assets\video\dance_03.mp4")  # Video local
cap = cv2.VideoCapture(0) # cámara

# Obtener propiedades del video original
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # Ancho de los frames
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Alto de los frames
fps = int(cap.get(cv2.CAP_PROP_FPS))                    # FPS del video original (no siempre es confiable)

# Para guardar el video procesado (desactivado por ahora)
# output_video = "procesado.mp4"
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para .mp4
# out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

# Iniciar el modelo Holistic de MediaPipe
with mp_holistic.Holistic(
        static_image_mode=False,  # El modelo trata cada frame como parte de un video
        # Usa la compejidad 1, modelo estándar, equilibrado entre precisión y velocidad
        # Por cuestiones, Google está desactivando lentamente Holisitic de MediaPipe
        model_complexity=1) as holistic:

    # Iniciar contador de tiempo para cálculo de FPS
    prev_time = 0

    while True:
        # Leer un frame del video o cámara
        ret, frame = cap.read()
        if not ret:
            break  # Si no se pudo leer, salimos del bucle

        # Redimensionar frame antes de pasarlo a RGB y procesarlo
        # Esto hace el código más eficiente
        small_frame = cv2.resize(frame, (640, 480))  # o incluso 320x240 si es aceptable
        frame_rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Procesar el frame con el modelo Holistic
        results = holistic.process(frame_rgb)

        # Dibujo de landmarks (puntos clave) con el mismo mediapipe

        # Rostro con malla facial
        mp_drawing.draw_landmarks(
            frame, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION,
            mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1),
            mp_drawing.DrawingSpec(color=(0, 128, 255), thickness=2))

        # Mano izquierda en azul
        mp_drawing.draw_landmarks(
            frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2, circle_radius=1),
            mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2))

        # Mano derecha en verde
        mp_drawing.draw_landmarks(
            frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=1),
            mp_drawing.DrawingSpec(color=(57, 143, 0), thickness=2))

        # Postura corporal en morado
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(128, 0, 255), thickness=2, circle_radius=1),
            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))

        # Calcular FPS actuales
        curr_time = time.time()
        fps_text = 1 / (curr_time - prev_time) if (curr_time - prev_time) > 0 else 0
        prev_time = curr_time

        # Mostrar FPS en la esquina superior izquierda
        cv2.putText(frame, f"FPS: {int(fps_text)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        # Mostrar el frame procesado en una ventana
        cv2.imshow("Frame", frame)

        # Guardar el frame si se descomenta esta línea
        # out.write(frame)

        # Salir al presionar ESC (código 27)
        if cv2.waitKey(1) & 0xFF == 27:
            break

# Liberar recursos al finalizar
cap.release()
# out.release()  # Solo si se guarda video
cv2.destroyAllWindows()
