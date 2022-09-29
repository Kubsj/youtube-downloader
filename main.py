from pytube import YouTube
from colorama import Fore
import title
title.titlescreen("RED")
print(Fore.BLUE + "Please input your youtube link below:")
link = input(">")
print("")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
print(Fore.BLUE + "Video title: " + Fore.RED + yt.title)
print(Fore.BLUE + "Resolution: " + Fore.RED + ys.resolution)
ys.download("")
print(Fore.RED + ("download has been completed"))
