from tkinter import *
from pytube import *

#Skeleton of tkinter
root = Tk()

save_path = "C:/Users/Loki/Videos/PY_YT_Videos"

#We can use the .grid directlyy along while declaring the variables
#But it is easier on the eyes to do it on the next line as done here

def extractURL():
    dVideo(url.get())

def extractPURL():
     i = 0
     Purl = Playlist(purl.get())
     for video in Purl.videos:
         watch__url = video.watch_url
         i +=1
         dPVideo(watch__url, i)

def extractCURL():
    i = 0
    Curl = Channel(curl.get())
    for video in Curl.videos:
        watch_url = video.watch_url
        i +=1
        dPVideo(watch_url, i)


#Download single video and shorts
def dVideo(url):
    url = YouTube(url)
    vtitle = url.title
    url = url.streams.filter(progressive=True, file_extension="mp4")
    high_res = url.get_highest_resolution()
    high_res.download(output_path=save_path)
    dComplete = Label(root, text=f"Download Complete : {vtitle}")
    dComplete.grid(row = 4, column = 1)

#Download playlist videos and channel videos    
def dPVideo(url, i):
    url = YouTube(url)
    vtitle = url.title
    url = url.streams.filter(progressive=True, file_extension="mp4")
    high_res = url.get_highest_resolution()
    high_res.download(output_path=save_path)
    dComplete = Label(root, text=f"Downloaded {i} Videos")
    dComplete.grid(row = 7, column = 1)


filler1 = Label(root, text="------------------------------")
filler1.grid(row = 0, column = 0)

mainLabel = Label(root, text="Youtube Downloader")
mainLabel.grid(row = 0, column = 1)

filler2 = Label(root, text="------------------------------")
filler2.grid(row = 0, column = 2)

filler3 = Label(root, text=" ")
filler3.grid(row = 4, column = 1)

filler4 = Label(root, text=" ")
filler4.grid(row = 7, column = 1)

filler5 = Label(root, text=" ")
filler5.grid(row=9, column = 1)

download_video = Label(root, text = "Video URL")
download_video.grid(row=3, column = 0)

url = Entry(root, width=50)
url.grid(row =3, column = 1)

dVideoButton = Button(root, text = "Download", padx=20, pady=5, bg = "black", fg = "white", command=extractURL)
dVideoButton.grid(row = 3, column = 2)

download_playlist = Label(root, text="Playlist URL")
download_playlist.grid(row=6, column = 0)

purl = Entry(root, width=50)
purl.grid(row=6, column=1)

dPlaylistButton = Button(root, text="Download", padx=20, pady=5, bg="black", fg="white", command=extractPURL)
dPlaylistButton.grid(row=6, column=2)

download_channel = Label(root, text = "Channel URL")
download_channel.grid(row = 8, column = 0)

curl = Entry(root, width=50)
curl.grid(row=8, column=1)

dChannelButton = Button(root, text="Download", padx=20, pady=5, bg="black", fg="white", command=extractCURL)
dChannelButton.grid(row=8, column=2)

root.mainloop()