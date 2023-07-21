import pytube
check = "1"
while check == "1":
    print()
    link= input("enter a YouTube video link -> ").strip()
   
    yt = pytube.YouTube(link)
    
    print()
    print("title: ", yt.title)
    print("views: ", yt.views)
    print("channel url:", yt.channel_url)
    print("decription:", yt.description)

    print()
    print("Enter 1 for Video or 2 for mp3")
    print()
    wanna_download = input("-> ")

    print("downloading.....")

    path = "youtube"
    stream = yt.streams

    if wanna_download == "1":
        video = stream.filter(progressive = True, file_extension = "mp4").first()
    else:
        video = stream.filter(only_audio=True).first()
        
    video.download(path)

    print("downloading copleted chack youtube folder")
    print()

    print("Do you want to use another link?")
    print("Enter 1 for YES or 2 for NO")
    print()
    check = input("-> ").strip()
