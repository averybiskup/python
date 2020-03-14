import pyshark
from socket import socket, AF_INET, SOCK_STREAM
capture = pyshark.LiveCapture(interface='en0', bpf_filter='port 5588', display_filter='tcp')
# capture.set_debug()
capture.sniff(timeout=0)
print('ready')
#
# s = socket(AF_INET, SOCK_STREAM)
# s.connect(('172.65.244.248', 5588))

while True:
    for packet in capture.sniff_continuously(packet_count=100):
        try:
            ip_dst = packet.ip.dst
            ip_src = packet.ip.src
            stream = packet.data.data.binary_value.decode('utf-8')

            if 'chatm' in stream:
                # print(stream)
                if "zone~" in stream:
                    chat = stream.split('zone~')[1]
                    user = chat.split('%')[1]
                    text = chat.split('%')[0]
                    print('Public:', user, " | ", text, chat.split('%')[2:4])
                    # print('TEST: ', chat)
                if "guild~" in stream:
                    # print('GUILD')
                    chat = stream.split('zone~')[1]
                    user = chat.split('%')[0]
                    text = chat.split('%')[1]
                    print('Guild:', user, " | ", text)
            if "xt%zm%mv" in stream:
                player_id = stream.split('%')[4]
                x = stream.split('%')[5]
                y = stream.split('%')[6]
                print(player_id, 'moved: ', x, y)
                # print('Move:', x, y)
            else:
                pass
                # print("NON CHAT: ", stream)

        except:
            pass
# s.send(bytearray('%xt%zm%mv%26827%295%200%10%', 'utf-8'))
# data = s.recv(1024)
# print(data)
# s.close()
