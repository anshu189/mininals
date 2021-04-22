'''
Author: Anshu Saini
GitHub: https://github.com/anshu189
Mail: anshusaini189381@gmail.com
Requirements: pytube, os (pip install pytube)
Program: YouTube Video Downloader

'''

import pytube
import os

users = os.getlogin()

url = input("Give URL:")

pytube.YouTube(url).streams.get_highest_resolution().download(f'C:/users/{users}/desktop')
