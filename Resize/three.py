import sys
import os

def resize_video():
    while True:  # Creo un menú para interactuar con el user
        try:
            result = int(
                input("Choose one os these options of resize a Video. '1','2','3' or '4' (0=return to main menu): \n"
                      "1. 720p \n"
                      "2. 480p \n"
                      "3. 240p \n"
                      "4. 120p \n"))
        except ValueError:
            print("You must to enter a number.")
            continue
        if result == 1:
            os.system("ffmpeg -i Big_Buck_Bunny_60fps_1080p.mp4 -vf scale=1280:720 Big_Buck_Bunny_60fps_720p.mp4")
            continue
        elif result == 2:
            os.system("ffmpeg -i Big_Buck_Bunny_60fps_1080p.mp4 -vf scale=858:480 Big_Buck_Bunny_60fps_480p.mp4")
            continue
        elif result == 3:
            os.system("ffmpeg -i Big_Buck_Bunny_60fps_1080p.mp4 -vf scale=360:240 Big_Buck_Bunny_60fps_240p.mp4")
            continue
        elif result == 4:
            os.system("ffmpeg -i Big_Buck_Bunny_60fps_1080p.mp4 -vf scale=160:120 Big_Buck_Bunny_60fps_120p.mp4")
            continue
        elif result == 0:  # Para salir del programa
            break
        elif result != 1 and result != 2 and result != 3 and result != 4:
            print("You must enter '1' or '2'.")
            continue
