import re
import tkinter as tk

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

    kwargs = {'tiktok_url': url, 'headless': True}
    if len(re.findall(r'[\w\W]+', tiktok_name.get())) > 0:
        kwargs['video_name'] = tiktok_name.get()
    api = SeleniumUtils(update_ui, **kwargs)
    api.download_video()
    button["state"] = "normal"


if __name__ == '__main__':
    window = tk.Tk()
    screen_width = GetSystemMetrics(0)
    screen_height = GetSystemMetrics(1)
    window.geometry(f"{int(screen_width / 3)}x{int(screen_height / 3.5)}")
    window.winfo_toplevel().title("Tiktok no watermark downloader")
    tiktok_hint = tk.Label(
        text="Enter tiktok video url\n an example is like this:\n"
             "https://www.tiktok.com/@luadoll/video/6974240019078794497")

    tiktok_url = tk.Entry()

    info = tk.Label(text="", fg='#0000CD')
    tiktok_name_hint = tk.Label(
        text="Enter the video name to be saved, if you leave it blank,\n video id will be used")
    tiktok_name = tk.Entry()

    button = tk.Button(text="Download video", command=launch_download)

    tiktok_hint.pack()
    tiktok_url.pack()
    tiktok_name_hint.pack()
    tiktok_name.pack()
    info.pack()
    button.pack()

    window.mainloop()
