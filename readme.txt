
# insta_yt_download
My first project on Prepleaf by Masai

on vscode editor this code is needed python library to run

    1 pytube
    2 instaloader

    for instal this library go to
        terminal
            new terminal
            use below commond
                pip install instaloader
                pip install pytube



if you face Error in the youtube download like:

    raise RegexMatchError(caller="get_transform_object", pattern=pattern)
    pytube.exceptions.RegexMatchError: get_transform_object: could not find match for var for={(.*?)};

ctrl + click on file derectory like: 
    PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\
    local-packages\Python311\site-packages\pytube\cipher.py

comment or remove line:
    226-227
    229
    245-252

hope it will work
