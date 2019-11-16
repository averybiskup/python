from appscript import app, mactypes

def set_image(file):
    file = 'images/' + file
    app('Finder').desktop_picture.set(mactypes.File(file))
