from pytube import YouTube
from colorama import Fore
try:
    import ascii
    ascii.titlescreen()
except:
    print(Fore.RED + "YOUTUBE DOWNLOADER")

while True:
    try:
        print(Fore.BLUE + "Please input your youtube link below:")
        link = input(Fore.RED + ">")
        print("")      
        yt = YouTube(link)


        ys = yt.streams.get_highest_resolution()

        print(Fore.BLUE + "Video title: " + Fore.RED + yt.title)
        print(Fore.BLUE + "Author " + Fore.RED + yt.author)
        print(Fore.BLUE + "Resolution: " + Fore.RED + ys.resolution)
        print(Fore.BLUE + "Video lengh: " + Fore.RED + str(yt.length) + Fore.BLUE + " seconds.")

        ys.download("")
        print(Fore.RED + ("download has been completed"))
    except:
        print("Please enter a valid youtube link")