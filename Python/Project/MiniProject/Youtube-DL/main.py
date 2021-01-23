import pytube

print("Bitte die Video URL eintragen: ")
url = input()
youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download()
