from package import Youtube

upload_info = {
    "title": "rema calm down",
    "description": "Another banger",
    "video": "C:/Users/HP/Desktop/youtube automation video/channels/4th.mp4",
    "thumbnail": "",
    "category": "Music",
    "privacy": "Public",
    "tags": ["rema", "banger", "loudness", "music", "holiday"],
    "kids": False
}

Youtube("./cookies.json", upload_info, True).upload()