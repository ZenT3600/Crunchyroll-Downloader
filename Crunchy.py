from requests_html import HTMLSession
import time
import os


def read_downloads():
    with open("downloads.txt", "r") as f:
        return f.readlines()


class CrunchyDownloader:
    def __init__(self, series, lang):
        self.series = series
        self.lang = lang
        self.session = HTMLSession()
        self.req = self.session.get(series)
        self.req.html.render()
    
    def download(self):
        try:
            os.mkdir("Downloads")
        except:
            pass
        try:
            title = self.req.html.find(".ellipsis")[0].text
            os.mkdir(f"Downloads\\{title}")
        except:
            pass
        links = [link.absolute_links for i, link in enumerate(self.req.html.find(".hover-bubble"))]
        for i in range(4):
            links.pop(len(links)-1)
        links.reverse()
        print(f"LINKS: {links}")
        for i, link in enumerate(links):
            link = "".join(link)
            print(f"LINK: {link}")
            os.system(f"youtube-dl --sub-lang {self.lang} --write-sub --output \"Downloads\\{title}\\Episode-{i+1}.mp4\" {link}")
            time.sleep(2)


if __name__ == "__main__":
    try:
        downloads = read_downloads()
        lang = input("Language: ")
        if len(lang) != 4:
            raise Exception
        for download in downloads:
            c = CrunchyDownloader(download, lang)
            c.download()
    except:
        print("Error, Exiting")
