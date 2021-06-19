import re
import tkinter as tk

from win32api import GetSystemMetrics

from selenuim_utils import SeleniumUtils


def update_ui(text):
    info.config(text=text)
    window.update()


def launch_download():
    button["state"] = "disabled"
    window.update()
    url = tiktok_url.get()
    match = re.match(r'https://www.tiktok.com/@(?!.*\.\.)(?!.*\.$)[^\W][\w.]{2,24}/video/[\d]+([?][\w])*',
                     url.strip())
    if match is None:
        info.config(text=f'Invalid tiktok url')
        button["state"] = "normal"
        return

    kwargs = {'tiktok_url': url, 'headless': False}
    proxy_password = re.findall(r'[\w\d]+://[\w\d.*+_?!]+:[\w\d.*+_?!]+@[\d.]+:[\d]+', tiktok_proxy.get().strip())
    proxy_no_password = re.findall(r'[\w\d]+://[\d.]+:[\d]+', tiktok_proxy.get().strip())
    if len(proxy_password) > 0 or len(proxy_no_password) > 0:
        kwargs['proxy'] = tiktok_proxy.get().strip()

    if len(re.findall(r'[\w\W]+', tiktok_name.get().strip())) > 0:
        kwargs['video_name'] = tiktok_name.get().strip()
    try:
        api = SeleniumUtils(update_ui, **kwargs)
        api.download_video()
    except Exception as e:
        update_ui(f"{e}")
    button["state"] = "normal"


if __name__ == '__main__':
    window = tk.Tk()
    screen_width = GetSystemMetrics(0)
    screen_height = GetSystemMetrics(1)
    window.geometry(f"{int(screen_width / 3)}x{int(screen_height / 3)}")
    window.winfo_toplevel().title("Tiktok no watermark downloader")
    tiktok_hint = tk.Label(
        text="Enter tiktok video url\n an example is like this:\n"
             "https://www.tiktok.com/@luadoll/video/6974240019078794497")

    tiktok_url = tk.Entry()

    info = tk.Label(text="", fg='#0000CD')
    tiktok_name_hint = tk.Label(
        text="Enter the video name to be saved, if you leave it blank,\n video id will be used")
    tiktok_name = tk.Entry()
    tiktok_proxy_hint = tk.Label(
        text="If video download failed,you might want to use a custom proxy,\n "
             "A proxy must follow the following pattern \n"
             "protocol://username:password@ip:port\n"
             "Leave it empty if you don't have one")
    tiktok_proxy = tk.Entry()

    button = tk.Button(text="Download video", command=launch_download)

    tiktok_hint.pack()
    tiktok_url.pack()
    tiktok_name_hint.pack()
    tiktok_name.pack()
    tiktok_proxy_hint.pack()
    tiktok_proxy.pack()
    info.pack()
    button.pack()

    window.mainloop()
