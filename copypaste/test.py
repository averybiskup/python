from AppKit import NSPasteboard, NSStringPboardType

pb = NSPasteboard.generalPasteboard()

pbstring = pb.stringForType_(NSStringPboardType)

with open('/Users/averybiskup/code/python/copypaste/log.txt', 'a+') as file:
    file.write(repr(pbstring) + "\n")
