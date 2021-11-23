import sys
import os


def yuv_histogram():

    os.system("ffmpeg -i Big_Buck_Bunny_60fps_1080p.mp4 -vf split=2[a][b],[b]histogram,"
              "format=yuv420p[hh],[a][hh]overlay videoplusYUV.mp4")

