import re

import requests
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumUtils:
    def __init__(self, **kwargs):
        self.url = kwargs.get('tiktok_url', 'https://www.tiktok.com/@amara.mari/video/6974391789390187777')
        self.video_name = kwargs.get('video_name', re.findall(r'/video/([\d]+)', self.url)[0] + ".mp4")
        self.headless = kwargs.get('headless', True)
        options = Options()
        options.headless = self.headless
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2)  # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', '/tmp')
        profile.set_preference("media.volume_scale", "0.0")
        self.browser = webdriver.Firefox(options=options, firefox_profile=profile,
                                         executable_path=r'geckodriver.exe', service_args=["--marionette-port", "2828"])
        self.wait = WebDriverWait(self.browser, 10, poll_frequency=1,
                                  ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

    def download_video(self):

        print('Please wait while we find your video')
        self.browser.get('https://ssstik.io/')

        text_url = self.wait.until(EC.presence_of_element_located(
            (By.ID, "main_page_text")))
        text_url.send_keys(self.url)

        text_submit = self.browser.find_element_by_id('submit')
        text_submit.click()

        no_watermark_button = self.wait.until(
            lambda x: x.find_element_by_xpath("//*[contains(text(), 'Without watermark [2]')]"))

        no_watermark_button.click()

        main_handler = self.browser.current_window_handle
        video_url = None
        for handle in self.browser.window_handles:
            if handle != self.browser.current_window_handle:
                self.browser.switch_to.window(handle)
                self.wait.until(
                    lambda x: x.find_element_by_tag_name("video"))
                video_url = self.browser.current_url
                self.browser.close()
                self.browser.switch_to.window(main_handler)

                break
        print(f'Video found downloading {self.video_name} please wait')

        r = requests.get(video_url, allow_redirects=True)

        with open(f'{self.video_name}.mp4', "wb") as f:
            f.write(r.content)
            print(f'Video {self.video_name} downloaded successfully')
        self.browser.close()
