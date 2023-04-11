import socket
import base64
from CRC_16_XMODEM import crc16_xmodem

def Demo():
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 通过套接字与X70建立连接
    a.connect(tuple(('10.10.10.111', 2929)))
    # 帧头
    frame_header = b'\x02'
    # 帧地址
    frame_addres1 = b'0'
    frame_addres2 = b'0'
    # 帧类型
    frame_type1 = b'0'
    frame_type2 = b'1'
    # 转换成16进制整数，进行crc检验
    check_code = (frame_addres1 + frame_addres2 + frame_type1 + frame_type2).hex()
    # crc检验
    check_code = crc16_xmodem(check_code)
    # check_code转为字节，格式为'\x**\x**'
    check_code = base64.b16decode(check_code.upper())
    # 帧尾
    frame_end = b'\03'
    # 组合帧Data
    data = frame_header + frame_addres1 + frame_addres2 + frame_type1 + frame_type2 + check_code + frame_end
    # 发送数据
    a.send(data)
    # 接受返回数据
    msg = a.recv(1024)
    # 断开连接
    a.close()
    print(msg.hex())
Demo()
