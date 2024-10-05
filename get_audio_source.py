"""
Script to display the avaliable audio sources
"""

from pyaudio import PyAudio

def get_audio_source() -> None:
    """Displays audio sources and their IDs"""
    pyaudio = PyAudio()
    info = pyaudio.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for device in range(0, numdevices):
        if (pyaudio.get_device_info_by_host_api_device_index(0, device).get('maxInputChannels')) > 0:
            print("Input Device id ", device, " - ", pyaudio.get_device_info_by_host_api_device_index(0, device).get('name'))

if __name__ == '__main__':
    get_audio_source()
