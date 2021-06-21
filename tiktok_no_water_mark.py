import argparse
import re
import sys
import tkinter as tk

from win32api import GetSystemMetrics

from selenuim_utils import SeleniumUtils


def update_info(text):
    if no_gui:
        print(text)
    else:
        info.config(text=text)
        window.update()


def launch_download():
    if not no_gui:
        button["state"] = "disabled"
        window.update()
        url = tiktok_url.get()
        proxy = tiktok_proxy.get().strip()
        output = tiktok_name.get().strip()
    else:
        url = args.url
        proxy = args.proxy if args.proxy is not None else ''
        output = args.output if args.output is not None else ''

    match = re.match(r'https://www.tiktok.com/@(?!.*\.\.)(?!.*\.$)[^\W][\w.]{2,24}/video/[\d]+([?][\w])*',
                     url.strip())
    if match is None:
        update_info(f'Invalid tiktok url')
        if not no_gui:
            button["state"] = "normal"
        return

    kwargs = {'tiktok_url': url, 'headless': not non_headless}
    proxy_password = re.findall(r'[\w\d]+://[\w\d.*+_?!]+:[\w\d.*+_?!]+@[\d.]+:[\d]+', proxy)
    proxy_no_password = re.findall(r'[\w\d]+://[\d.]+:[\d]+', proxy)
    if len(proxy_password) > 0 or len(proxy_no_password) > 0:
        kwargs['proxy'] = proxy
    else:
        if len(proxy) > 0:
            update_info(f'Invalid proxy scheme,try again or leave the proxy field empty if you don\'t have one')

            button["state"] = "normal"
            return
    if len(re.findall(r'[\w\W]+', output)) > 0:
        kwargs['video_name'] = output

    api = SeleniumUtils(update_info, **kwargs)
    try:
        api.download_video()
    except Exception:
        update_info(f"Server failed to deliver a response, consider using "
                    f"or updating your proxy\n and retry again")
        api.browser.close()
    if not no_gui:
        button["state"] = "normal"


def check_executable():
    return re.match(r'[\w\W]*.exe$', sys.argv[0]) is not None


if __name__ == '__main__':
    is_executable = check_executable()
    parser = argparse.ArgumentParser(description="A script to download tiktok videos without watermarks")
    parser.add_argument('-ng', '--no-gui', default=False, action='store_true', help='Launch the script without GUI')
    parser.add_argument('-url', help="tiktok video url\n an example is like this:\n"
                                     "https://www.tiktok.com/@luadoll/video/6974240019078794497", )
    parser.add_argument('-o', '--output', help="Specify thr file name in which the output file will be named in", )
    parser.add_argument('-p', '--proxy', help="A proxy must follow the following pattern \n"
                                              "protocol://username:password@host:port\n", )
    parser.add_argument('-nh', '--non-headless', default=False, action='store_true',
                        help="Launch the web browser in non headless mode", )

    args = parser.parse_args()
    if is_executable:
        args.func(args)
    if '-url' not in sys.argv and ('-ng' in sys.argv or '--no-gui' in sys.argv):
        raise parser.error('You must specify the tiktok url using -url in non gui mode')
    no_gui = args.no_gui
    non_headless = args.non_headless
    window = tk.Tk()
    if no_gui:
        launch_download()
        sys.exit()
    screen_width = GetSystemMetrics(0)
    screen_height = GetSystemMetrics(1)
    window.geometry(f"{int(screen_width / 2.5)}x{int(screen_height / 3)}")
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
             "protocol://username:password@host:port\n"
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
