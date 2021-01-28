# File Variable Component
import PySimpleGUI as sg
import numpy as np
import layout as ly
import cv2
window = sg.Window(title="KIRANA GUI CAM", layout=ly.layout2, location=(0, 0))


class imgToBytes:

    def __init__(self, name, inputName, inputFrame):
        self.key = inputName
        self.frame = inputFrame
        self.name = name
        self.name = cv2.imencode(".png", self.frame)[1].tobytes()
        window[self.key].update(data=self.name)


def RacikBolaD(frame):
    event, values = window.read(1)
    h_min_fr_ball = int(values["-H_MIN_FR_BALL-"])
    s_min_fr_ball = int(values["-S_MIN_FR_BALL-"])
    v_min_fr_ball = int(values["-V_MIN_FR_BALL-"])
    global orangeD
    # Untuk  mengembalikan array baru dari bentuk dan jenis yang diberikan, diisi dengan nilai satu
    kernel = np.ones((5, 5), np.uint8)
    # untuk meng-convert image matrix ke grayscale dengan parameter cv2.COLOR_BGR2GRAY
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerO = np.array([h_min_fr_ball, s_min_fr_ball, v_min_fr_ball])
    upperO = np.array([31, 255, 255])
    orangeD = cv2.inRange(hsv, lowerO, upperO)
    orangeD = cv2.erode(orangeD, kernel)
    # Membuat Opening (yaitu mengurangi noise di luar kontour warna)
    orangeD = cv2.morphologyEx(orangeD, cv2.MORPH_OPEN, kernel)
    # Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
    orangeD = cv2.morphologyEx(orangeD, cv2.MORPH_CLOSE, kernel)
    return orangeD


def RacikLapanganD(frame):
    event, values = window.read(1)
    h_min_fr_field = int(values["-H_MIN_FR_FIELD-"])
    s_min_fr_field = int(values["-S_MIN_FR_FIELD-"])
    v_min_fr_field = int(values["-V_MIN_FR_FIELD-"])
    kernel = np.ones((5, 5), np.uint8)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    global hijauD
    lowerH = np.array([h_min_fr_field, s_min_fr_field, v_min_fr_field])
    upperH = np.array([102, 255, 255])
    hijauD = cv2.inRange(hsv, lowerH, upperH)
    hijauD = cv2.erode(hijauD, kernel)
    # Membuat Opening (yaitu mengurangi noise di luar kontour warna)
    hijauD = cv2.morphologyEx(hijauD, cv2.MORPH_OPEN, kernel)
    # Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
    hijauD = cv2.morphologyEx(hijauD, cv2.MORPH_CLOSE, kernel)
    return hijauD


def RacikBolaA(frameUp):
    event, values = window.read(1)
    h_min_up_ball = int(values["-H_MIN_UP_BALL-"])
    s_min_up_ball = int(values["-S_MIN_UP_BALL-"])
    v_min_up_ball = int(values["-V_MIN_UP_BALL-"])
    global orangeA
    # Untuk  mengembalikan array baru dari bentuk dan jenis yang diberikan, diisi dengan nilai satu
    kernel = np.ones((5, 5), np.uint8)
    # untuk meng-convert image matrix ke grayscale dengan parameter cv2.COLOR_BGR2GRAY
    hsv = cv2.cvtColor(frameUp, cv2.COLOR_BGR2HSV)
    lowerO = np.array([h_min_up_ball, s_min_up_ball, v_min_up_ball])
    upperO = np.array([31, 255, 255])
    orangeA = cv2.inRange(hsv, lowerO, upperO)
    orangeA = cv2.erode(orangeA, kernel)
    # Membuat Opening (yaitu mengurangi noise di luar kontour warna)
    orangeA = cv2.morphologyEx(orangeA, cv2.MORPH_OPEN, kernel)
    # Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
    orangeA = cv2.morphologyEx(orangeA, cv2.MORPH_CLOSE, kernel)
    return orangeA


def RacikLapanganA(frameUp):
    event, values = window.read(1)
    h_min_up_field = int(values["-H_MIN_UP_FIELD-"])
    s_min_up_field = int(values["-S_MIN_UP_FIELD-"])
    v_min_up_field = int(values["-V_MIN_UP_FIELD-"])
    kernel = np.ones((5, 5), np.uint8)
    hsv = cv2.cvtColor(frameUp, cv2.COLOR_BGR2HSV)
    global hijauA
    lowerH = np.array([h_min_up_field, s_min_up_field, v_min_up_field])
    upperH = np.array([102, 255, 255])
    hijauA = cv2.inRange(hsv, lowerH, upperH)
    hijauA = cv2.erode(hijauA, kernel)
    # Membuat Opening (yaitu mengurangi noise di luar kontour warna)
    hijauA = cv2.morphologyEx(hijauA, cv2.MORPH_OPEN, kernel)
    # Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
    hijauA = cv2.morphologyEx(hijauA, cv2.MORPH_CLOSE, kernel)
    return hijauA