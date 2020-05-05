import pyshark
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, IPPROTO_TCP
import time
import select
import sys
import os
import pyperclip


try:
    collect = int(sys.argv[1])
except:
    collect = 0

if collect:
    capture = pyshark.LiveCapture(interface='en0', bpf_filter='port 5588', display_filter='tcp')
    # capture.set_debug()
    capture.sniff(timeout=0)

while collect:
    for packet in capture.sniff_continuously(packet_count=100):
        try:
            ip_dst = packet.ip.dst
            ip_src = packet.ip.src
            stream = packet.data.data.binary_value.decode('utf-8')
            # print(stream)

            if 'chatm' in stream:
                # print(stream)
                if "zone~" in stream:
                    chat = stream.split('zone~')[1]
                    user = chat.split('%')[1]
                    text = chat.split('%')[0]
                    print('Public:', user, " | ", text, chat.split('%')[2:4])
                    player_id = chat.split('%')[2]
                    # print(player_id)
                    # print(stream, ip_src, '=>', ip_dst)

                    if 'vie' not in user.lower():
                        pyperclip.copy(text)

                if "guild~" in stream:
                    # print('GUILD')
                    chat = stream.split('zone~')[1]
                    user = chat.split('%')[0]
                    text = chat.split('%')[1]
                    print('Guild:', user, " | ", text)
            if "xt%zm%mv" in stream:
                player_id = stream.split('%')[4]
                print(stream, ip_src, '=>', ip_dst)
                x = stream.split('%')[5]
                y = stream.split('%')[6]
                # print(player_id, 'moved: ', x, y)
                # print('Move:', x, y)
            else:
                pass
                # print("NON CHAT: ", stream)

        except:
            pass

def sendPacket(packet):
    try:
        ready_to_read, ready_to_write, in_error = select.select([s,], [s,], [], 5)
        # print(ready_to_read, '\n', ready_to_write, '\n', in_error)
        # data = s.recv(100000)
        # if not data: return

        # s.send(bytearray(p, 'utf-8'))
        # s.send('b' + str(packet))
        # print(data)
        s.send(packet)
        # print(s.recvmsg(1024))
    except Exception as ex:
        print(ex)

p = b'%xt%zm%mv%156341%375%472%10%'
move = '%xt%zm%mv%640%392%200%10%'

# s = socket(AF_INET, SOCK  _STREAM)

IP = '172.65.244.248'
IPtest = '51.81.5.169'
dallas = '75.126.77.24'
japan = '192.50.157.155'

if not collect:
    try:

        s = socket(AF_INET, SOCK_STREAM, proto=IPPROTO_TCP)
        print('Socket Created')

        s.connect((IP, 5588))
        print('Connected')

        s.setblocking(True)
        s.send(b'%xt%zm%mv%156341%375%472%10%')

        # s.settimeout(10)
        sendPacket(p)
    except Exception as ex:
        print(ex)




# s.close()
