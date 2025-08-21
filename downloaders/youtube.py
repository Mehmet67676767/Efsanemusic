from os import path

from yt_dlp import YoutubeDL

from config import DURATION_LIMIT
from helpers.errors import DurationLimitError


ydl_opts = {
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "cookiefile": "cookies.txt",  # YouTube cookie desteği
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)
    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"This video is too long: {duration} minutes."
        )
    return ydl.prepare_filename(info)
