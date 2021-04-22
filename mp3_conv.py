'''
Author: Anshu Saini
GitHub: https://github.com/anshu189
Mail: anshusaini189381@gmail.com
Requirements: moviepy (pip install moviepy)
Program: Video to Audio Convertor(OFFLINE)

'''

from moviepy.editor import VideoFileClip


def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()


name = input("Enter the file name/path: ")
convert_to_mp3(name)
