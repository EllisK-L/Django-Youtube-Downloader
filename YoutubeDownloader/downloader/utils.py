import youtube_dl


def getVid(link):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

    with ydl:
        result = ydl.extract_info(
            link,
            download=False # We just want to extract the info
        )

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result

    print(video)
    print(video_url)


def checkLink(link):
    print(link)

if __name__ == "__main__":
    getVid("https://www.youtube.com/watch?v=rU0f4kmBpX8")