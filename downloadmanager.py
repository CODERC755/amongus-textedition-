
import wget
import os

url = 'https://gitcdn.link/cdn/CODERC755/secret-game-files/main/game.py?token=GHSAT0AAAAAABQEX6KMLOPWPOEN2WN7ZDLAYUMADJQ'
wget.download(url)

os.remove("./launch.bat")
os.remove("./downloadmanager.py")
