from pathlib import Path
from typing import List
from app.core.errors import MoveFilesError
from app.services.file_service import move_files_to_new_folder
from pytube import Playlist, YouTube
from app.core.log import LighRedLogger

ConsoleMessage = LighRedLogger("INFO")

def get_user_input():
    playlist_url = input(f"Gib den Link zur Playlist ein: ")
    return playlist_url


def display_playlist_contents(playlist):
    print("Die Playlist enthält die folgenden Videos:")
    for video in playlist:
        print(video)


def prompt_continue():
    while True:
        user_input = input("Möchtest du fortfahren? (Y/n): ").lower()
        if user_input in ['y', 'n']:
            return user_input == 'y'
        else:
            print("Ungültige Eingabe. Bitte gib 'Y' für Ja oder 'n' für Nein ein.")


def get_download_folder():
    download_folder = input("Gib den Namen des Download-Ordners ein: ")
    return download_folder


def display_completion_message(download_folder):
    ConsoleMessage(f"Der Download wurde abgeschlossen! Die Dateien befinden sich im Ordner: {download_folder}")


def main():
    try:
        ConsoleMessage("Hallo Patrik")
        playlist_url = get_user_input()
        playlist = Playlist(playlist_url).video_urls

        display_playlist_contents(playlist)

        if not prompt_continue():
            ConsoleMessage("Der Vorgang wurde abgebrochen.")
            return

        download_folder = get_download_folder()

        for video in playlist:
            yt = YouTube(url=video).streams.get_audio_only().download()

        move_files_to_new_folder(".", download_folder, ".mp4")

        display_completion_message(download_folder)

    except Exception as e:
        print(f"Fehler aufgetreten: {e}")


if __name__ == "__main__":
    main()
