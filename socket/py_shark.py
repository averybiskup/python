import pyshark
capture = pyshark.LiveCapture(interface='en0', bpf_filter='port 5588', display_filter='tcp')
# capture.set_debug()
capture.sniff(timeout=60)
while True:
    for packet in capture.sniff_continuously(packet_count=5):
        try:
            ip_dst = packet.ip.dst
            ip_src = packet.ip.src
            stream = packet.data.data.binary_value.decode('utf-8')
            print(stream)
        except:
            print('No DATA')
