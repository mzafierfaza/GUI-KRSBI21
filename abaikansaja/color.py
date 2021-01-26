import vr
import cv2


    


# contourBola = cv2.findContours(vr.orangeD, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
#     if len(contourBola) > 0:
#         area = max(contourBola, key=cv2.contourArea)
#         xx, yy, w, h = cv2.boundingRect(area)
#         ((x, y), radius) = cv2.minEnclosingCircle(area)
#         approx = cv2.approxPolyDP(area, 0.001*cv2.arcLength(area, True), True)
#         if area is not None:
#             cv2.drawContours(frame, [approx], 0, (0, 0, 255), 2)
#  ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==  
       
#     contourLapangan = cv2.findContours(vr.hijauD, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
#     if len(contourLapangan) > 0:
#         area = max(contourLapangan, key = cv2.contourArea)
#         approx = cv2.approxPolyDP(area, 0.001*cv2.arcLength(area, True), True)
#         if area is not None: 
#             cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)  #Untuk menggambar kontur fungsi 
#             # cv2.line(frame, (pusat),(int(320), int(240)), (0,255,0), 1)
# ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==  
#     contourLapangan_omni = cv2.findContours(vr.hijauA, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
#     if len(contourLapangan_omni) > 0:
#         area = max(contourLapangan_omni, key = cv2.contourArea)
#         approx = cv2.approxPolyDP(area, 0.001*cv2.arcLength(area, True), True)
#         if area is not None: 
#             cv2.drawContours(frameUp, [approx], 0, (0, 255, 0), 2)