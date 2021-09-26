from pytube import YouTube

url = input("Enter YT url"+"\n")

yt = YouTube(url)

print(yt.title + "\n" + yt.views + "\n" +yt.length +"\n\n")
print("Available Streams : \n", yt.streams.filter(progressive = True), "\n\n")

tag = input("Enter your stream tag")
ys = yt.streams.get_by_itag(tag)
ys.download()