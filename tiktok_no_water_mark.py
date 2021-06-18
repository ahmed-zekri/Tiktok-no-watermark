import re
import sys

from selenuim_utils import SeleniumUtils

if __name__ == '__main__':

    match = None
    while match is None:
        url = input('Please enter a valid tiktok url\n')
        match = re.match(r'https://www.tiktok.com/@(?!.*\.\.)(?!.*\.$)[^\W][\w.]{2,24}/video/[\d]+([?][\w])*',
                         url.strip())
        if match is None:
            print(f'Invalid tiktok url')
            sys.exit()
        api = SeleniumUtils(tiktok_url=url, headless=False)
        api.download_video()
