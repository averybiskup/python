from appscript import app, mactypes
app('Finder').desktop_picture.set(mactypes.File('test.jpg'))
