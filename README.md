# P2_VideoEndodingUPF
That's the second Lab of Audio and Video Encoding made by Víctor Zaldivar. The main purpose for the lab is to implement the ‘ffmpeg’ through python scripts.
First thing that I did was download the BBB video from internet with a resolution of 1920x1080 and with 60 frames per second. \n
Every task of the lab is divided in a different directory inside the project folder. Although, inside each directory we can find the python script corresponding to the task, the video outputs because of the task and a ‘__init__’ python script that I use it to be able to import all the scripts and the functions of the lab that are in different directories through the ‘main’ script. By calling the main script, you are able to run all the program and iterate between all the tasks. 
The first Task consist of trim the BBB video. To do it, the program ask you by the terminal in which minutes and second would you start trimming the video and the minutes and seconds to end the trim. You must put a value between 0 and 59 in both cases (for minutes and seconds), if not, the ‘ffmpeg’ won’t apply the trim. Also, if the time to start the trim are bigger than the end, the ‘ffmpeg’ will fail. The output video trimmed would be store it as ‘trimmedVideo.mp4’.
The second Task consist of extract the YUV histogram from the BBB video and then create a new Video showing both elements at the same time, the video and the corresponding YUV histogram from the video. The output video file of this task is saved as ‘videoplusYUV’ inside the ‘YUV_histogram’ directory.
The third Task consist of change the resolution of the BBB video in 4 different sizes. For that, I create a menu for the user to be able to select which resolution wants to resize the original video. The output files are in the Resize directory, each one with the corresponding resolution indicated. The input file will always be the same (1080p) to avoid problems to try improving the resolution, because it’s impossible to do through ‘ffmpeg’.
Finally, the last Task consist of changing the channel or changing the audio codec. First, we call a menu to decide if the user wants to decide between both options. If the user selects the first one, as the original BBB audio is in stereo (2-channels), the code call to other functions to change the channel audio from stereo to mono. The output file is saved as ‘MONO_Big_Buck_Bunny_60fps_1080p.mp4’ in ‘channel_audioCodec’ directory. On the other hand, if the user selects the second option, the code call to other function to change the container of the audio codec. The BBB video contains the ‘acc’ audio codec and the programs only allows the user to change to mp3 or mp2. The corresponding files are saved as ‘audioCodec=mp3.mp4’ and ‘audioCodec=mp2.mp4’ respectively. 

**PROBLEMS**
The only thing that I have been missing to implement is to store all the output files inside the corresponding directory for each task. I have not been able to find a command in the ‘ffmpeg’ library to implement that, so the outputs of all tasks will be stored inside the project main folder. 


