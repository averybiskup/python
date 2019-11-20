from appscript import app, mactypes

def set_image(file):
    file = file
    app('Finder').desktop_picture.set(mactypes.File(file))
