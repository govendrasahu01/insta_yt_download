def main(insta_yt):
    if insta_yt == "1":
        print()
        print("You have selected Instagram")

        import insta

    elif insta_yt == "2":
        print()
        print("You have selected YouTube")
        print()

        import yt  
    else:
        print("Enter only 1 for Instagram or 2 for YouTube")
        insta_yt = input("->  ")
        main(insta_yt)


print()
print("what do you want to use Instagram or YouTube?")
print()
print("use 1 for Instagram")
print("use 2 for YouTube")

insta_yt = input("->  ")
print()
main(insta_yt)


