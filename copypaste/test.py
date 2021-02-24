<<<<<<< HEAD
# gets the latest string from the clipboard


=======
>>>>>>> 513c0536dcc53d44b93fd84637f62f5d1eb77121
from AppKit import NSPasteboard, NSStringPboardType

pb = NSPasteboard.generalPasteboard()

pbstring = pb.stringForType_(NSStringPboardType)

with open('/Users/averybiskup/code/python/copypaste/log.txt', 'a+') as file:
    file.write(repr(pbstring) + "\n")
