# insta_yt_download
My first project on Prepleaf by Masai

on vscode editor, this code is needed Python library to run

    1 pytube
    2 instaloader

    To instal this library go to 
        terminal menu
            new terminal
            use below command
                pip install instaloader
                pip install pytube



if you face an Error in the youtube download like:

    raise RegexMatchError(caller="get_transform_object", pattern=pattern)
    pytube.exceptions.RegexMatchError: get_transform_object: could not find match for var for={(.*?)};

ctrl + click on file directory like: 
    PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\
    local-packages\Python311\site-packages\pytube\cipher.py

comment or remove the line from cipher.py:
    226-227
    229
    245-252

hope it will work