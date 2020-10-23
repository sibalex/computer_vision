import numpy as np
import cv2

cap = cv2.VideoCapture(0)


def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)


def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)


def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)


def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)


# make_480p()
# make_720p()
# change_res(1280, 720)


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


while True:
    rect, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # frame30 = rescale_frame(frame, percent=30)
    # cv2.imshow('frame30', frame30)

    frame50 = rescale_frame(frame, percent=50)  # размер окна
    # img = cv2.cvtColor(frame50, cv2.COLOR_BGR2HSV)
    img = cv2.cvtColor(frame50, cv2.COLOR_BGR2GRAY)  # фильтр цвета

    """ GaussianBlur( кадр, размер ядра, отклонение)
    размер ядра — список из двух чисел (x,y), которые задают размер ядра фильтра Гаусса по горизонтали и вертикали. \
    Чем больше ядро, тем более размытым станет кадр;
    отклонение — стандартное отклонение по оси X."""
    img2 = cv2.GaussianBlur(img, (5, 5), 2)  # размытие кадра (Размытие по Гауссу)

    # cv2.imshow('frame51', img)
    cv2.imshow('frame50', img2)

    # frame150 = rescale_frame(frame, percent=150)
    # cv2.imshow('frame150', frame150)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# ip cam
# VideoCapture("rtsp://username:password@ip-address")
