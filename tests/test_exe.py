import subprocess


def launch_tiktok(index, url):
    global successful_downloads
    subprocess.run(['tiktok_no_water_mark.exe', '-ng', '-url', url, '-p', proxies[index]], check=True)
    successful_downloads += 1
    print(successful_downloads)


if __name__ == '__main__':
    successful_downloads = 0
    proxies = ['protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
               'protocol://ip:username@password:password']
    urls = ['https://www.tiktok.com/@dr.dinahussein/video/6974029037123407105?lang=en&is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@abumashal04/video/6975983753701149954?lang=en&is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@abdallahenawy/video/6975567866397609221?lang=en&is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@ahmed_yahia998/video/6974822658785512709?lang=en&is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@monasheikh_/video/6974446194105912577?lang=en&is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@youssefismailmusic/video/6973686418220649733?lang=en&is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@imen_q/video/6968093927459081478?lang=en&is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@imen_q/video/6970448098652966149?lang=en&is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@imen_q/video/6971861064296254726?is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@imeen_amouna/video/6968321236820643078?is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@roses_are_rosie/video/6943422805467745537?is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@bts_official_bighit/video/6964945720885464322?is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@myvtc/video/6960685846068481282?is_copy_url=1&is_from_webapp=v1',
            'https://www.tiktok.com/@abdoalkanj2/video/6966693368004971782?is_copy_url=1&is_from_webapp=v1']
    index = 0

    for url in urls:
        launch_tiktok(index, url)
        index += 1
        if index > len(proxies):
            index = 0
