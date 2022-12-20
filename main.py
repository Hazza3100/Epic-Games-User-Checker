import random
import requests
import threading


checked = []
class EpicScraper:
    def __init__(self) -> None:
        self.session = requests.Session()

    def getUser(self):
        try:
            username = ''.join(random.choices('poiuytrewqlkjhgfdsamnbvcxz', k=4))
            if username in checked:
                return ''.join(random.choices('poiuytrewqlkjhgfdsamnbvcxz', k=4))
            else:
                checked.append(username)
                return username
        except:
            raise "Username Creation Error"

    def check(self):
        while True:
            try:
                with self.session as session:
                    username = self.getUser()
                    proxy = random.choice(open('proxies.txt', 'r').read().splitlines())
                    proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
                    headers = {'authority': 'fortnitetracker.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','referer': 'https://fortnitetracker.com/profile/search?q=gfgd','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',}

                    response = session.get(f'https://fortnitetracker.com/profile/all/{username}', headers=headers, proxies=proxies)
                    if response.status_code == 200:
                        print("taken")
                    if response.status_code == 404:
                        print("Available")
                        open('available.txt', 'a').write(f'{username}\n')
                    if response.status_code == 429:
                        print("Rate limited")
            except Exception as x:
                pass



threads = int(input("threads"))
for i in range(threads):
    threading.Thread(target=EpicScraper().check).start()
