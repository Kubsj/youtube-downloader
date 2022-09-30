from asyncio.windows_events import NULL
from cgitb import reset
from pytube import YouTube
from colorama import Fore
import ascii


ascii.titlescreen()

print(Fore.BLUE + "Please input your youtube link below:")
link = input(Fore.RED + ">")
print("")

while True:
    try:
        
        yt = YouTube(link)
        break
    except:
        continue


ys = yt.streams.get_highest_resolution()

print(Fore.BLUE + "Video title: " + Fore.RED + yt.title)
print(Fore.BLUE + "Author " + Fore.RED + yt.author)
print(Fore.BLUE + "Resolution: " + Fore.RED + ys.resolution)
print(Fore.BLUE + "Video lengh: " + Fore.RED + str(yt.length) + Fore.BLUE + " seconds.")

ys.download("")
print(Fore.RED + ("download has been completed"))
