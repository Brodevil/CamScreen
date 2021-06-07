from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime


screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
captured_screen = cv2.VideoWriter(f"CamScreen ({time_stamp}).mp4", fourcc, 10.0, (screen_width, screen_height))



while True:
    img = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("CamScreen", img_final)
    captured_screen.write(img_final)
    if cv2.waitKey(10) == ord("q"):
        break

