import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

year_to_travel_to = input("Which year do you want to travel to? Format: YYYY-MM-DD: ")

billboard_url = f"https://appbrewery.github.io/bakeboard-hot-100/{year_to_travel_to}/"
header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0"}

response = requests.get(billboard_url, headers=header)
response.raise_for_status()
html = response.text

soup = BeautifulSoup(html, "html.parser")
song_title = soup.find_all(name="h3", class_="chart-entry__title")

song_list = []

for song in song_title:
    song = song.get_text()
    song_list.append(song)

yt = YTMusic("browser.json")
playlists = yt.get_library_playlists()

playlist_exists = False

for name in playlists:
    if name["title"] == year_to_travel_to:
        playlist_exists = True
        break

if playlist_exists:
    raise SystemExit("Playlist already exists")
else:
    playlist_id = yt.create_playlist(
        title=year_to_travel_to,
        description="Python project",
        privacy_status="PRIVATE",
    )

video_ids = []

for song in song_list:
    song = song.strip()
    try:
        results = yt.search(
            query=song,
            filter="songs",
            limit=1,
        )

        if results:
            video_ids.append(results[0]["videoId"])
            print(f"{song} Added")
    except Exception as e:
        print(f"Error with {song}: {e}")

if video_ids:
    yt.add_playlist_items(
        playlistId=playlist_id,
        videoIds=video_ids,
    )
