#  -*- coding: utf-8 -*-
from tqdm import tqdm
import requests
 
 
 

url="https://cdnm.meln.top/mr/Aventura%20-%20Cuando%20Volveras.mp3?session_key=69e46c3bf738ecc46eb521c7547462f2&hash=04042964424a6d1682b5f315d3188253"
file=requests.get(url,stream=True)
size=int(file.headers['Content-Length'])
 
bar=tqdm(range(size),desc="Downloading...:",ncols=100)

fw=open("file.mp3","wb")

for bs in file.iter_content(chunk_size=1024):
    bar.update(len(bs))
    fw.write(bs)




fw.close()



chunk=1024
bar=tqdm(iterable=file.iter_content(chunk_size = chunk),total=size/chunk)