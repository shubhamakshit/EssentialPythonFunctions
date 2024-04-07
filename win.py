from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import os
import ctypes

class WinUtiks:
    @staticmethod
    def change_wallpaper(path):
        if os.path.exists(path) and os.path.isfile(path):
            SPI_SETDESKWALLPAPER = 20 
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
        else:
            print(f"No file found at: {path}")

    @staticmethod
    def mute_audio():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # Mute the volume
        volume.SetMute(1, None)

    @staticmethod
    def lock_screen():
        ctypes.windll.user32.LockWorkStation()

    @staticmethod
    def shutdown():
        os.system("shutdown /s /t 1")

    @staticmethod
    def restart():
        os.system("shutdown /r /t 1")

    @staticmethod
    def log_off():
        os.system("shutdown /l")

    @staticmethod
    def get_ip_address():
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address







# usage
# WinUtiks.change_wallpaper("C:\\path\\to\\your\\image.jpg")
# WinUtiks.mute_audio()
