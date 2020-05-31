import os

speed = input('speed:')

os.system('defaults write -g InitialKeyRepeat -int ' + speed)
