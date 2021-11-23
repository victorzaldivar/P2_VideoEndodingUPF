import Trim.one
import YUV_histogram.two
import Resize.three
import channel_audioCodec.four


header = """
    ################################
       #### P2 - More FFMPEG ####
    ################################
     ## Made by Víctor Zaldívar ##"""

main_options = """
What do you want to do?
    1.- Trim a Video
    2.- Extract the YUV histogram from a video 
    3.- Change the resolution of a video
    4.- Change stereo/mono and audio coded
    0.- Exit"""

def show_menu():

    print(header)

    exit_game = False
    while not exit_game:
        print(main_options)

        selected_option = input()
        if selected_option == "0":
            exit_game = True

        elif selected_option == "1":
            Trim.one.trim_video()

        elif selected_option == "2":
            YUV_histogram.two.yuv_histogram()

        elif selected_option == "3":
            Resize.three.resize_video()

        elif selected_option == "4":
            channel_audioCodec.four.change_channel_audioCoded()

        else:
            print("This is not a valid option! Let's try again...")


if __name__ == '__main__':
    show_menu()