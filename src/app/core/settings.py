from pathlib import Path
from datetime import datetime

# BASE_DOWNLOAD_DIRECTORY = Path(__file__).parents[3] / "downloads"

class DownloadConfig:

    def __init__(self, download_folder: Path = None) -> None:
        """
        Initializes the download configuration.

        Parameters:
            download_folder (Path): The base download directory.
        """
        self.download_folder = download_folder

    def generate_download_directory(self, playlist_name: str):
        """
        Generates the download directory for the specified playlist.

        Parameters:
            playlist_name (str): The name of the playlist.

        Returns:
            Path: The Path object for the download directory.
        """
        current_date = datetime.now().strftime("%Y-%m-%d")
        download_directory = self.download_folder / self.generate_folder_name(playlist_name, current_date)

        if download_directory.exists():
            duplicate_count = 1
            while download_directory.exists():
                download_directory = self.download_folder / self.generate_folder_name(playlist_name, current_date, duplicate_count)
                duplicate_count += 1

        download_directory.mkdir(parents=True, exist_ok=True)
        return download_directory

    @staticmethod
    def generate_folder_name(playlist_name: str, current_date: str, duplicate_count: int = None) -> str:
        if duplicate_count is not None:
            return f"{playlist_name} - {current_date} - ({duplicate_count})"
        else:
            return f"{playlist_name} - {current_date}"
