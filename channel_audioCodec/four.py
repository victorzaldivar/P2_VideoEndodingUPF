import sys
import os

def change_channel_audioCoded():
    while True:  # Creo un menú para interactuar con el user
        try:
            result = int(input("Choose one of these two options. (0=return to main menu): \n"
                               "1. Change the BBB video from stereo to mono \n"
                               "2. Change the audio codec from the BBB video \n"))
        except ValueError:
            print("You must to enter a number.")
            continue
        if result == 1:
            change_channel()
            continue
        elif result == 2:
            change_audio_codec()
            continue
        elif result == 0:  # Para volver al main menu
            break
        elif result != 1 and result != 2:
            print("You must enter '1' or '2'.")
            continue


def change_channel():
    os.system("ffmpeg -i Big_Buck_Bunny_60fps_1080p.mp4 -ac 1 MONO_Big_Buck_Bunny_60fps_1080p.mp4")


def change_audio_codec():
    while True:  # Creo un menú para interactuar con el user
        try:
            result = int(input("Choose one of these options to change the audio codec. (0=return): \n"
                               "1. mp3 \n"
                               "2. mp2 \n"))
        except ValueError:
            print("You must to enter a number.")
            continue
        if result == 1:
            os.system("ffmpeg -i Big_Buck_Bunny_60fps_1080p.mp4 -vcodec copy -acodec mp3 -ac 1 audioCodec=mp3.mp4")
            continue
        elif result == 2:
            os.system("ffmpeg -i Big_Buck_Bunny_60fps_1080p.mp4 -vcodec copy -acodec mp2 -ac 1 audioCodec=mp4.mp4")

        elif result == 0:  # Para salir del programa
            break
        elif result != 1 and result != 2:
            print("You must enter '1', '2'.")
            continue

