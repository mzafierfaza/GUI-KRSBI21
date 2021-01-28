import vr
import PySimpleGUI as sg
import cv2
import numpy as np
import layout as ly

cap = cv2.VideoCapture("../bll.mp4")        # ganti jadi sumber kamera
cap2 = cv2.VideoCapture("../bll2.mp4")


def constrain(val, min_val, max_val):  # Fungsi contrain untuk membatasi suatu nila
    # Fungsi return untuk mengembalikan nilai ke awal
    return min(max_val, max(min_val, val))

class deteksi:
    def __init__(self,name,posisi,color,colorLapangan):
        self.warnaLap = colorLapangan
        self.warna = color
        self.nama = name
        self.nama = cv2.findContours(self.warna, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
        res2 = cv2.bitwise_or(self.warna, self.warnaLap)

        if posisi == "Atas":
            framApprox = frameUp
        if posisi == "Depan":
            framApprox = frame
        if name == "Hijau":
            Approx = (0,255,0)
        if name == "Orange":
            Approx = (0,0,255)

        if len(self.nama) > 0:
            area = max(self.nama, key=cv2.contourArea)
            xx, yy, w, h = cv2.boundingRect(area)
            ((x, y), radius) = cv2.minEnclosingCircle(area)
            approx = cv2.approxPolyDP(area, 0.001*cv2.arcLength(area, True), True)
            maxxx = (xx+w)+3
            maxyy = (yy+h)+3
            huxx = xx+int(w/2)
            huyy = yy+int(h/2)
            maxXX = constrain(maxxx, 0, 479)
            maxYY = constrain(maxyy, 0, 319)
            huXX = constrain(huxx, 0, 479)
            huYY = constrain(huyy, 0, 319)
            if area is not None:
                if name == "Hijau":
                    cv2.drawContours(framApprox, [approx], 0, Approx, 2)
                elif name == "Orange":       # ini detek orange
                    # pass
                    # cv2.drawContours(framApprox, [approx], 0, Approx, 2)
                    if np.any(res2[maxYY,maxXX]) or  np.any(res2[huYY,maxXX]) or  np.any(res2[maxYY,huXX]) or  np.any(res2[maxYY,xx-5]) or  np.any(res2[huYY,xx-5]) != 0:       ## pengecekan kiri atas bola adalah lapangan
                        cv2.rectangle(framApprox, (xx,yy), (xx+w, yy+h), (0,165,255), 2)              #Membuat kotak pada gambar maupun kamera  real-time
                        cv2.putText(framApprox, ("(" + str(int(x)) + "," + str(int(y)) + ")"), (int(x) - 35, int(y) + 15),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2) #Menempatkan text
                        cv2.line(framApprox, (330,490),(int(x), int(y)), (255,255,255), 2)                                    
                        cv2.line(framApprox, ((int(x), int(y))),(int(xx-5), int(huYY)), (0,255,0), 1)
                        cv2.line(framApprox, ((int(x), int(y))),(int(xx-5), int(maxYY)), (0,255,0), 1)
                        cv2.line(framApprox, ((int(x), int(y))),(int(huXX), int(maxYY)), (0,255,0), 1)
                        cv2.line(framApprox, ((int(x), int(y))),(int(maxXX), int(huYY)), (0,255,0), 1)
                        cv2.line(framApprox, ((int(x), int(y))),(int(maxXX), int(maxYY)), (0,255,0), 1)
                        print("BOLA TERDETEKSI")
                        # arduino.write(str(x).encode())  #Untuk Mengirim data X ke arduino
                        # arduino.write('x'.encode())     
                        # arduino.write(str(y).encode())  #Untuk Mengirim data y ke arduino
                        # arduino.write('y'.encode())
                    else:
                        cv2.drawContours(framApprox, [approx], 0, Approx, 2)

            else:           ## Jika bola tidak terdeteksi
                if name == "Hijau":     ## Jika hijau tidak terdeteksi, pass yaudah
                    pass                ## ini memang pass, jangan dihapus
                elif name == "Orange":                   ## Jika orange tidak terdeteksi maka kirim 0 arduino
                    pass                ## hapus pass yang ini kalo nak coba
                    # print("BOLA NOTHING")
                    # arduino.write('0'.encode())
                    # arduino.write('x'.encode())
                    # arduino.write('0'.encode())
                    # arduino.write('y'.encode())
        elif len(self.nama) == 0:           ## Jika bola tidak ditekesi sama sekali
            if name == "Hijau":
                pass             ## ini memang pass, jangan dihapus
            elif name == "Orange":
                pass            ## hapus pass yang ini kalo nak coba
                # print("BOLA NOTHING")
                # arduino.write('0'.encode())
                # arduino.write('x'.encode())
                # arduino.write('0'.encode())
                # arduino.write('y'.encode())

        
while True:
    event, values = vr.window.read(1)
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    ret, frame = cap.read()
    ret2, frame2 = cap2.read()

    # frame = np.full((320, 480), 255)
    frame = cv2.resize(frame, (480, 320))
    frameUp = cv2.resize(frame2, (480, 320))
    
    vr.RacikBolaD(frame)
    vr.RacikLapanganD(frame)
    vr.RacikBolaA(frameUp)
    vr.RacikLapanganA(frameUp)

    frameBolaD = cv2.resize(vr.orangeD, (240, 150))
    frameLapanganD = cv2.resize(vr.hijauD, (240, 150))
    frameBolaA = cv2.resize(vr.orangeA, (240, 150))
    framelapanganA = cv2.resize(vr.hijauA, (240, 150))


    contourLapanganD = deteksi("Hijau", "Depan" , vr.hijauD, vr.orangeA)    
    contourLapanganA = deteksi('Hijau', "Atas", vr.hijauA, vr.orangeA)
    contourBolaD = deteksi("Orange", "Depan", vr.orangeD, vr.hijauD)    # argumen ke 4 hanya berlaku untuk mendeteksi bola di dalam lapangan
    contourBolaA = deteksi("Orange", "Atas", vr.orangeA, vr.hijauA)     # argumen ke 4 hanya berlaku untuk mendeteksi bola di dalam lapangan

    frameFront = vr.imgToBytes("imgFront", "-FRAME_FR-", frame)
    frameUpper = vr.imgToBytes("frameUpper", "-FRAME_UP-", frameUp)
    ballFront = vr.imgToBytes("ballFront", "-BALL_FR-", frameBolaD)
    fielFront = vr.imgToBytes("fielFront", "-FIELD_FR-", frameLapanganD)
    ballUpper = vr.imgToBytes("ballUpper", "-BALL_UP-", frameBolaA)
    fieldUpper = vr.imgToBytes("fieldUpper", "-FIELD_UP-", framelapanganA)


window.close()
