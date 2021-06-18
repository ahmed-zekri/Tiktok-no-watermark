import os
import re
import shutil
import sys
import tkinter as tk
from pathlib import Path

from win32api import GetSystemMetrics

from selenuim_utils import SeleniumUtils


def update_ui(text):
    info.config(text=text)
    window.update()


def launch_download():
    button["state"] = "disabled"
    url = tiktok_url.get()
    match = re.match(r'https://www.tiktok.com/@(?!.*\.\.)(?!.*\.$)[^\W][\w.]{2,24}/video/[\d]+([?][\w])*',
                     url.strip())
    if match is None:
        info.config(text=f'Invalid tiktok url')
        button["state"] = "normal"
        return
    api = SeleniumUtils(update_ui, tiktok_url=url, headless=True)
    api.download_video()
    button["state"] = "normal"


if __name__ == '__main__':
    window = tk.Tk()
    screen_width = GetSystemMetrics(0)
    screen_height = GetSystemMetrics(1)
    window.geometry(f"{int(screen_width / 2)}x{int(screen_height / 3)}")
    window.winfo_toplevel().title("Tiktok no watermark downloader")
    tiktok_hint = tk.Label(
        text="Enter tiktok video url\n an example is like this:\n"
             "https://www.tiktok.com/@luadoll/video/6974240019078794497")

    tiktok_url = tk.Entry()

    info = tk.Label(text="", fg='#0000CD')

    button = tk.Button(text="Download video", command=launch_download)

    tiktok_hint.pack()
    tiktok_url.pack()
    info.pack()
    button.pack()

    window.mainloop()
