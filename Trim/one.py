import sys
import os

def trim_video():
    while True:  # Creo un menú para interactuar con el user
        try:
            print("The length of the BBB video is 10 minutes and 34 seconds. Let's trim it!! \n")
            minStart = input("Select the minutes to start the trim of the video (0 to 59): ")
            secStart = input("Select the seconds to start the trim of the video (0 to 59): ")
            minEnd = input("Select the minutes to end the trim of the video (0 to 59): ")
            secEnd = input("Select the seconds to end the trim of the video (0 to 59): ")
            str1 = "ffmpeg -i Big_Buck_Bunny_60fps_1080p.mp4 -ss 00:"
            str2 = ":"
            str3 = " -to 00:"
            str4 = " -c:v copy -c:a copy trimmedVideo.mp4"
            finalstring = str1 + minStart + str2 + secStart + str3 + minEnd + str2 + secEnd + str4
            os.system(finalstring)
            break

        except ValueError:
            print("You must to enter a number between 0 and 59")
            continue









