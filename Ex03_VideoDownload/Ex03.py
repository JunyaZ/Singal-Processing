# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:08:36 2018

@author: ya000
"""

from pytube import YouTube as yt

def Procedure2_3(yt):
    title = yt.title
    thum = yt.thumbnail_url
    formats =yt.streams.all()
    stream  = yt.streams.first()
    stream.download()
    print("Title is", title)
    print(" Thum is ",thum)
    print("Media formats",formats)

def Procedure_4(yt):
    progressive = yt.streams.filter(progressive = True).all()
    DASH= yt.streams.filter(adaptive = True).all()
    audio = yt.streams.filter(only_audio = True).all()
    mp4= yt.streams.filter(file_extension = 'mp4').all()
    #prog_stream = progressive.streams.first()
    
    #Progress720 = yt.streams.get_by_res('720p')
    print(progressive)
    print(DASH)
    print(audio)
    print(mp4)
    progressive[0].download()
    #audio.download()
    #mp4.download()
    #Progress720.download()
"""       
def Defined_User(url):
    url = input(" Enter an url :" ,url)
    print (" The url is ", url)
    
"""
if __name__ == '__main__':
    yt = yt("https://www.youtube.com/watch?v=9bZkp7q19f0")
    Procedure2_3(yt)
    Procedure_4(yt)
    #url = input("Enter an url:")
    #print(" The url is ", url)
    #url = input("Enter he directory:")
    #print(" The url is ", url)
    