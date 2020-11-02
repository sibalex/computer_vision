# https://imageai.readthedocs.io/en/latest/
# https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Detection

# pip install tensorflow # ==1.13.1
# pip install opencv-python
# pip install keras # ==2.2.4
# pip install numpy # ==1.16.1
# pip install imageai --upgrade

# ------------------------- images -------------------------
# RetinaNet (Size = 145 mb, high performance and accuracy, with longer detection time)

from imageai.Detection import ObjectDetection
import os

exec_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(exec_path, "resnet50_coco_best_v2.0.1.h5")) # RetinaNet
detector.loadModel()

list = detector.detectObjectsFromImage(
    input_image=os.path.join(exec_path, "objects.jpg"),             # исходное изображение
    output_image_path=os.path.join(exec_path, "new_objects.jpg"),   # сохраняем полученное фото
    minimum_percentage_probability=70,                              # минимум точности
    display_percentage_probability=True,                            # отоброжать проценты
    display_object_name=False                                       # отоброжать имена
)


# ------------------------- video -------------------------
# https://imageai.readthedocs.io/en/latest/video/index.html
# YOLOv3 (Size = 237 mb, moderate performance and accuracy, with a moderate detection time)

from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolo.h5")) # YOLOv3
detector.loadModel()

video_path = detector.detectObjectsFromVideo(
    input_file_path=os.path.join(execution_path, "traffic.mp4"),        # видео для обработки
    output_file_path=os.path.join(execution_path, "traffic_detected"),  # видео после обработки
    frames_per_second=20,                                               # фреймы в секунде (по кадрово)
    log_progress=True                                                   # логи обработки в консоль
)

print(video_path)
