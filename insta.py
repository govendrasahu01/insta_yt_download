import instaloader

def intagram(is_insta_id):
        
        loader = instaloader.Instaloader()

        if is_insta_id == "1":
            insta_id(loader)
        elif is_insta_id == "2":
            insta_post_link(loader)
        else:
            print("Enter only 1 for insta id or 2 for insta post link")
            print()
            is_insta_id = input(" -> ").strip()
            intagram(is_insta_id)

def insta_id(loader):
    # download all post or dp --------------------------------------------

    # user like -> "govendrasahu01"
    print()
    user =  input("Instagram user id  -> ").strip()
    print()
    
    # print("Url:",user.external_url)
    # print("Bio:",user.biography)
    # print("Posts:",user.mediacount)
    # print("igtv:",user.igtvcount)
    # print()


    print("what do you want to download?")
    print("for dp only use -> 1 ")
    print("for all post use -> 2")
    print("if you put another value it will download dp only")
    print()

    is_only_dp = input("-> ").strip()
    print()
    print("downloading........")
    if is_only_dp == "2":
         is_only_dp = False
    else:
         is_only_dp = True
    
    try:
        loader.download_profile(user, profile_pic_only= is_only_dp)

        print("downloading success")
        print()
    except:
        print()
        print("Error: failed to download")
        print()

def insta_post_link(loader):
        
        post_link =  input("Enter instagram post link ->  ").strip() 
        print()  
        print("geting details:") 

        post = instaloader.Post.from_shortcode(loader.context, post_link.split("/")[-2])

        # Extract the post's caption
        caption = post.caption
        print("Caption: ", caption)
        num_likes = post.likes
        print("Likes: ", num_likes)
        
        print()


        print("do you want to download the post? ")
        print("Enter 1 for yes or 2 for no")

        wants_download_post = input("-> ").strip()
        if wants_download_post == "1":
            print()
            print("downloading.........")
            # download the post image or video
            loader.download_post(post,target='post')
            print()
            
            print("wow1! downloaded")
            print()
            print()
        else:
            exit


is_insta_id = input("Enter 1 for insta id or 2 for post link -> ").strip()
intagram(is_insta_id) 