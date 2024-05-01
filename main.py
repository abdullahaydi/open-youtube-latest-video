import scrapetube
import webbrowser
url = "freecodecamp"
videos = scrapetube.get_channel(channel_username=url,sort_by="newest",limit=1)

for video in videos:
    video_link=(video['videoId'])
link = "https://www.youtube.com/watch?v="+video_link
webbrowser.open(link)