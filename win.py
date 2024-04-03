import ctypes
import os

class WinUtiks:
    @staticmethod
    def change_wallpaper(path):
        if os.path.exists(path) and os.path.isfile(path):
            SPI_SETDESKWALLPAPER = 20 
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
        else:
            print(f"No file found at: {path}")

# usage
# WinUtiks.change_wallpaper("C:\\path\\to\\your\\image.jpg")
