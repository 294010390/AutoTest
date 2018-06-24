#_*_coding:utf-8_*_

import serial
import threading
from time import *
from Original_Command import *
import json

def readdata():
    f = open("COM_Config.json", encoding='utf-8')  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    setting = json.load(f)
    Port = setting['Port']   #注意多重结构的读取语法
    Speed = setting['Speed']

    data = [Port,Speed]
    return data

Port = readdata()[0]
Speed = readdata()[1]

print(Port)
print(Speed)

ser = serial.Serial(Port,Speed)  # Serial类实例化一个对象

class COMTrans(object):
    '''
    定义串口发送和接收功能；
    RunRecv()函数没有参数，打印接收的串口数据；
    RunSend(data)，参数data：需要发送的数据；如发送字符串"root",则data='root'.encode('utf-8')
    '''

    def Recv():
        while True:
            count = ser.inWaiting() #获取接收缓存区的字节数

            if count!=0: #如果有数据
                recv = ser.read(count)  #读取数据
                currenttime = strftime("%Y-%m-%d %H:%M:%S",localtime(time())) #获取当前时间
                print(currenttime + '<< ' + recv.decode('utf-8'))

            ser.flushInput()    #清空缓存区
            sleep(0.5)   #延迟0.5s

    def RunRecv():
        t1 = threading.Thread(target=COMTrans.Recv)
        t1.start()

    def Send(data):
        ser.write(data)
        #sleep(1)

    def RunSend(data):
        t2 = threading.Thread(target=COMTrans.Send,args=[data,])
        t2.start()
        t2.join()

if __name__ == '__main__':
    try:
        #COMTrans.RunRecv()  #接收串口数据
        command = MDCCOMMAND()

        # COMTrans.RunSend('\r\n'.encode('utf-8'))
        # sleep(1)
        # COMTrans.RunSend('root\r\n'.encode('utf-8'))
        # sleep(1)
        # COMTrans.RunSend('cd /opt\r\n'.encode('utf-8'))
        # sleep(2)
        # COMTrans.RunSend('./Serclient\r\n'.encode('utf-8'))
        # sleep(2)

        #Send_Command每个操作只需要Retuen即可，不需要数据转换
        COMTrans.RunSend(command.Touch_Down(120,100))
        sleep(0.2)
        COMTrans.RunSend(command.Touch_Up(120,100))
        print("Touch")
        sleep(2)

        COMTrans.RunSend(command.Hardkey_Home_Down())
        sleep(0.2)
        COMTrans.RunSend(command.Hardkey_Home_Up())
        sleep(2)

        COMTrans.RunSend(command.Volume_Right())
        sleep(2)

        COMTrans.RunSend(command.Hardkey_Home_Down())
        sleep(0.2)
        COMTrans.RunSend(command.Hardkey_Home_Up())
        sleep(2)

        COMTrans.RunSend(command.Volume_Left())
        sleep(2)



    except KeyboardInterrupt:   #按下ctrl-C时需将串口关闭
        if ser!=None:
            ser.close()