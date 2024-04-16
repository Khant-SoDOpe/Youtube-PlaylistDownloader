import re
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
DOWNLOAD_DIR = '/Users/khant/Downloads/Nodejs'

playlist = Playlist('https://www.youtube.com/watch?v=auZ50D2aAK4&list=PLOmL3sL-afbSlct9s9zJXV7KVeyXWQy9e&pp=iAQB')

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))

a = 0

for url in playlist.video_urls:
    print(url)

# physically downloading the audio track
for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(output_path=DOWNLOAD_DIR)
    print(a)
    a += 1
