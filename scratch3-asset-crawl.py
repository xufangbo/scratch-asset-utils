# from StringIO import StringIO
import getopt
import gzip
import json
import sys
import os
import requests
import urllib
import re

pretend = False
downloaded = set()
cdn = 'http://cdn.assets.scratch.mit.edu'
proxies = { 'http': '10.198.157.119:9400','https': '10.198.157.119:9400'}

def download_file(url, path):
    if os.path.exists(path):
        # print("skip:" + path)
        return
    floder = "/".join(path.split("/")[0:-1])
    if not os.path.exists(floder):
        os.makedirs(floder)
    res = requests.get(url,proxies=proxies,verify=False) # 添加了,verify=False
    if path in downloaded:
        return None
    if res.status_code == 200:
        with open(path, "wb") as f:
            f.write(res.content)
            downloaded.add(path)
            return res.content
    else:
        return None


def download_media(json_path):
    print(json_path);
    if not json_path: return None
    media_url = "https://cdn.assets.scratch.mit.edu/internalapi/asset/%s/get/"
    thumbnails_url = "https://cdn.scratch.mit.edu/scratchr2/static/__628c3a81fae8e782363c36921a30b614__/medialibrarythumbnails/8d508770c1991fe05959c9b3b5167036.gif"
    download_path = "scratch3/internalapi/asset/"
    json_name = json_path.split("/")[-1]

    with open(json_path, "r",encoding="utf8") as f:
        items = json.load(f)
        for item in items:            
            if json_name == "sprites.json":
                for sound in item.get('sounds', []):
                    md5 = sound['md5ext']
                    download_file(media_url % md5, download_path + md5)
                for costume in item.get('costumes', []):
                    md5 = costume['md5ext']
                    download_file(media_url % md5, download_path + md5)
            else:
                res = download_file(media_url % item['md5ext'], download_path + item['md5ext'])


requests.packages.urllib3.disable_warnings() # s. https不进行安全验证时不输出警告日志

download_media("scratch3/json_index/backdrops.json")
download_media("scratch3/json_index/costumes.json")
download_media("scratch3/json_index/sounds.json")
download_media("scratch3/json_index/sprites.json")
