import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_drawing_style=mp.solutions.drawing_styles

mp_drawing_specs=mp_drawing.DrawingSpec(color=(0,255,0),thickness=2)

mp_face_mesh=mp.solutions.face_mesh
cap=cv2.VideoCapture('v1.mp4')
# #############################################################################################


with mp_face_mesh.FaceMesh(
    max_num_faces=6,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
    ) as face_mesh:

   while cap.isOpened():
        ret,img=cap.read()
        img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        result=face_mesh.process(img_rgb)
    
        for face_landmark in result.multi_face_landmarks:
             mp_drawing.draw_landmarks(
                image=img,
                landmark_list=face_landmark,
                connections=mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=mp_drawing_specs,
                connection_drawing_spec=mp_drawing_style
            .get_default_face_mesh_contours_style()
            )
             
            #  mp_drawing.draw_landmarks(
            #     image=img,
            #     landmark_list=face_landmark,
            #     connections=mp_face_mesh.FACEMESH_TESSELATION,
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp_drawing_style
            # .get_default_face_mesh_tesselation_style()
            # )

             mp_drawing.draw_landmarks(
                image=img,
                landmark_list=face_landmark,
                connections=mp_face_mesh.FACEMESH_IRISES,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_style
                .get_default_face_mesh_iris_connections_style())

        cv2.imshow('face',img)

        if cv2.waitKey(10) & 0xFF==ord('q'):
            break

cap.release()
cv2.destroyAllWindows()