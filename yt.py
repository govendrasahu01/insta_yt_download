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
    print("Do you want to download? ")
    print("Enter 1 for YES or 2 for NO")
    print()
    wanna_download = input("-> ")

    if wanna_download == "1":
        print("downloading.....")

        path = "youtube"
        stream = yt.streams
        video = stream.filter(progressive = True, file_extension = "mp4").first()
        video.download(path)

        print("downloading copleted chack youtube folder")
        print()

    print("Do you want to use another link?")
    print("Enter 1 for YES or 2 for NO")
    print()
    check = input("-> ").strip()
