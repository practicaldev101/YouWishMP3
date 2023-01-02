from pytube import YouTube, exceptions
from pytube.cli import on_progress
from colorama import Fore
import os
from os import path
import re
class Audio():

    def __init__(self, url: str) -> None:
        self.url = url
        self.directory = "downloads"

    def printMessage(self, text: str, color: str) -> None:
        tempColor = ""
        if color == "green":
            tempColor = Fore.LIGHTGREEN_EX
        elif color == "yellow":
            tempColor = Fore.LIGHTYELLOW_EX
        elif color == "red":
            tempColor = Fore.LIGHTRED_EX
        print(tempColor + text + Fore.RESET)
    
    def safetyFilename(self, text: str):
        modText = text.replace("|", "-").replace('/', '-').replace('\\', ',')
        
        emoji_pattern = re.compile(
            "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "]+", flags = re.UNICODE)
        return emoji_pattern.sub(r'', modText)
    
    def downloadAudio(self) -> True or False:
        try:
            self.video = YouTube(self.url, on_progress_callback=on_progress)
            self.printMessage("[ + ] Getting audio from video\n", "green")
            audio = self.video.streams.get_audio_only(subtype="webm")
            outputPath =  path.abspath("./" + self.directory)
            filename = u'' + self.safetyFilename(audio.title) + ".mp3"
            absFilePath = path.join(outputPath, filename)

            if path.exists(outputPath):
                self.printMessage("[ + ] Verifying that the file doesn't exist\n", "yellow")

                if path.exists(absFilePath) == False:
                    self.printMessage("[ + ] Downloading " + audio.title + "\n", "green")
                    audio.download(output_path=outputPath, filename=filename)
                    self.printMessage("\n[ + ] Audio " + audio.title + " downloaded" + "\n", "green")
                    return True
                else:
                    self.printMessage("[ ! ] The file '" + filename + "' exists...Skipping\n", "red")
                    return False
            else:
                self.printMessage("[ ! ] The directory " + self.directory +" doesn't exist, creating new one\n", "yellow")
                os.mkdir(outputPath)
                self.downloadAudio()
        except exceptions.RegexMatchError:
            self.printMessage("\n[ ! ] It looks like URL video is invalid.\n", "red")
            self.printMessage("[ ! ] URL: " + self.url + "\n", "yellow")
            return False;
