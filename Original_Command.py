#_*_coding:utf-8_*_
from ctypes import *
from time import *
from Serial import *

EVENT_LEFTDOWN = 0
EVENT_LEFTUP = 1
EVENT_MMOUSEMOVE = 2
EVENT_KEYDOWN = 3
EVENT_KEYUP = 4
EVENT_LEFTROTATE = 5
EVENT_RIGHTROTATE = 6

HARDKEY_MOUSE = 0
HARDKEY_HOME = 0x66
HARDKEY_PREVIOUS = 0x6c
HARDKEY_NEXT = 0x67
HARDKEY_MEDIA = 0xe2
HARDKEY_ROTATE = 0x01

class MDCCOMMAND1(Structure):
    '''
    定义发送命令的结构体
    '''
    _fields_ = [
        ('dwLengthPackage', c_int),
        ('dwCommand', c_int),
        ('dwIndex', c_int),
        ('dwErrorCode', c_int),
        ('dwFileSize', c_int),
        ('event', c_ushort),
        ('key', c_ushort),
        ('x', c_ushort),
        ('y', c_ushort),
        ('steps', c_ushort),
        ('end', c_ushort),
    ]

class MDCCOMMAND(object):
    '''
    定义了以下几个命令：
    1.Touch_Down(self,_x,_y)，参数是Touch的坐标；
    2.Touch_Down(self,_x,_y)，参数是Touch的坐标；

    注：完成一个操作需要执行Down,然后休眠一段时间（短按默认0.5s，长按可设置3s），最后执行Up
    '''
    def __init__(self):
        self.newMDCCOMMAND = MDCCOMMAND1()
        self.newMDCCOMMAND.dwLengthPackage = 0x20
        self.newMDCCOMMAND.dwCommand = 0
        self.newMDCCOMMAND.dwIndex = 0
        self.newMDCCOMMAND.dwErrorCode = 0
        self.newMDCCOMMAND.dwFileSize = 0
        self.newMDCCOMMAND.event = 0
        self.newMDCCOMMAND.key = 0
        self.newMDCCOMMAND.x = 0
        self.newMDCCOMMAND.y = 0
        self.newMDCCOMMAND.steps = 0
        self.newMDCCOMMAND.end = 0

    #-------------------------------------------------------------------------------
    #传输touch down：
    def Touch_Down(self,_x,_y):

        self.newMDCCOMMAND.event = EVENT_LEFTDOWN
        self.newMDCCOMMAND.key = HARDKEY_MOUSE
        self.newMDCCOMMAND.x = _x
        self.newMDCCOMMAND.y = _y
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND

    # 传输touch down：
    def Touch_Up(self,_x,_y):

        self.newMDCCOMMAND.event = EVENT_LEFTUP
        self.newMDCCOMMAND.key = HARDKEY_MOUSE
        self.newMDCCOMMAND.x = _x
        self.newMDCCOMMAND.y = _y
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND


    # 传输touch mobe：
    def Touch_Move(self,_x,_y):

        self.newMDCCOMMAND.event = EVENT_MMOUSEMOVE
        self.newMDCCOMMAND.key = HARDKEY_MOUSE
        self.newMDCCOMMAND.x = _x
        self.newMDCCOMMAND.y = _y
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND

    # HOME键按下：
    def Hardkey_Home_Down(self):
        self.newMDCCOMMAND.event = EVENT_KEYDOWN
        self.newMDCCOMMAND.key = HARDKEY_HOME
        self.newMDCCOMMAND.x = 0
        self.newMDCCOMMAND.y = 0
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND

    # HOME键释放：
    def Hardkey_Home_Up(self):
        self.newMDCCOMMAND.event = EVENT_KEYUP
        self.newMDCCOMMAND.key = HARDKEY_HOME
        self.newMDCCOMMAND.x = 0
        self.newMDCCOMMAND.y = 0
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND

    # Previous键按下：
    def Hardkey_Previous_Down(self):
        self.newMDCCOMMAND.event = EVENT_KEYDOWN
        self.newMDCCOMMAND.key = HARDKEY_PREVIOUS
        self.newMDCCOMMAND.x = 0
        self.newMDCCOMMAND.y = 0
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND



    # Previous键释放：
    def Hardkey_Previous_Up(self):
        self.newMDCCOMMAND.event = EVENT_KEYUP
        self.newMDCCOMMAND.key = HARDKEY_PREVIOUS
        self.newMDCCOMMAND.x = 0
        self.newMDCCOMMAND.y = 0
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND

    # Next键按下：
    def Hardkey_Next_Down(self):

        self.newMDCCOMMAND.event = EVENT_KEYDOWN
        self.newMDCCOMMAND.key = HARDKEY_NEXT
        self.newMDCCOMMAND.x = 0
        self.newMDCCOMMAND.y = 0
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND



    # Next键释放：
    def Hardkey_Next_Up(self):
        self.newMDCCOMMAND.event = EVENT_KEYUP
        self.newMDCCOMMAND.key = HARDKEY_NEXT
        self.newMDCCOMMAND.x = 0
        self.newMDCCOMMAND.y = 0
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND

    # Media键按下：
    def Hardkey_Media_Down(self):
        self.newMDCCOMMAND.event = EVENT_KEYDOWN
        self.newMDCCOMMAND.key = HARDKEY_MEDIA
        self.newMDCCOMMAND.x = 0
        self.newMDCCOMMAND.y = 0
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND

    # Media键：
    def Hardkey_Media_Up(self):

        self.newMDCCOMMAND.event = EVENT_KEYUP
        self.newMDCCOMMAND.key = HARDKEY_MEDIA
        self.newMDCCOMMAND.x = 0
        self.newMDCCOMMAND.y = 0
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND

    # 左旋x下：
    def Volume_Left(self):
        self.newMDCCOMMAND.event = EVENT_LEFTROTATE
        self.newMDCCOMMAND.key = HARDKEY_ROTATE
        self.newMDCCOMMAND.x = 0
        self.newMDCCOMMAND.y = 0
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND

    # 右旋x下：
    def Volume_Right(self):
        self.newMDCCOMMAND.event = EVENT_RIGHTROTATE
        self.newMDCCOMMAND.key = HARDKEY_ROTATE
        self.newMDCCOMMAND.x = 0
        self.newMDCCOMMAND.y = 0
        self.newMDCCOMMAND.steps = 0

        return self.newMDCCOMMAND

class Commands(object):
    '''
    定义了基本的操作;
    1.InitHandShake(),每次重启之后需要执行这个函数；
    2.PressMediakey(),按下Media硬按键
    3.PressHomekey(),按下Home硬按键
    4.PressNextkey(),按下Next硬按键
    5.PressPreviouskey(),按下Previous硬按键
    6.VolumeDecrease(),音量-1
    7.VolumePlus(),音量+1
    8.TouchScreen(x,y)，Touch屏幕，参数为坐标(x,y)
    9.DragLeft(),拖拽到前一个画面
    10.DragRight(),拖拽到前后一个画面
    11.DragDown),向下拖拽
    12.DragUp(),向上拖拽
    DragLeft
    '''

    def __init__(self):
        self.command = MDCCOMMAND()

    def InitHandShake(self):
        '''
        初始化，在Radio内运行Serclient,接收命令
        '''
        COMTrans.RunSend('\r\n'.encode('utf-8'))
        sleep(1)
        COMTrans.RunSend('root\r\n'.encode('utf-8'))
        sleep(1)
        COMTrans.RunSend('cd /opt\r\n'.encode('utf-8'))
        sleep(2)
        COMTrans.RunSend('./Serclient\r\n'.encode('utf-8'))
        sleep(2)

    def PressMediakey(self):
        COMTrans.RunSend(self.command.Hardkey_Media_Down())
        sleep(0.2)
        COMTrans.RunSend(self.command.Hardkey_Media_Up())
        sleep(2)

    def PressHomekey(self):
        COMTrans.RunSend(self.command.Hardkey_Home_Down())
        sleep(0.2)
        COMTrans.RunSend(self.command.Hardkey_Home_Up())
        sleep(2)

    def PressNextkey(self):
        COMTrans.RunSend(self.command.Hardkey_Next_Down())
        sleep(0.2)
        COMTrans.RunSend(self.command.Hardkey_Next_Up())
        sleep(2)

    def PressPreviouskey(self):
        COMTrans.RunSend(self.command.Hardkey_Previous_Down())
        sleep(0.2)
        COMTrans.RunSend(self.command.Hardkey_Previous_Up())
        sleep(2)

    def VolumeDecrease(self):
        COMTrans.RunSend(self.command.Volume_Left())
        sleep(2)

    def VolumePlus(self):
        COMTrans.RunSend(self.command.Volume_Right())
        sleep(2)

    def TouchScreen(self, _x, _y):
        COMTrans.RunSend(self.command.Touch_Down(_x, _y))
        sleep(0.2)
        COMTrans.RunSend(self.command.Touch_Up(_x, _y))
        sleep(2)

    def DragLeft(self):
        COMTrans.RunSend(self.command.Touch_Down(200, 200))
        COMTrans.RunSend(self.command.Touch_Move(220, 200))
        COMTrans.RunSend(self.command.Touch_Move(240, 200))
        COMTrans.RunSend(self.command.Touch_Move(260, 200))
        COMTrans.RunSend(self.command.Touch_Move(280, 200))
        COMTrans.RunSend(self.command.Touch_Move(300, 200))
        COMTrans.RunSend(self.command.Touch_Up(320, 200))

    def DragRight(self):
        COMTrans.RunSend(self.command.Touch_Down(320, 200))
        COMTrans.RunSend(self.command.Touch_Move(300, 200))
        COMTrans.RunSend(self.command.Touch_Move(280, 200))
        COMTrans.RunSend(self.command.Touch_Move(260, 200))
        COMTrans.RunSend(self.command.Touch_Move(240, 200))
        COMTrans.RunSend(self.command.Touch_Move(220, 200))
        COMTrans.RunSend(self.command.Touch_Up(200, 200))

    def DragDown(self):
        COMTrans.RunSend(self.command.Touch_Down(400, 320))
        COMTrans.RunSend(self.command.Touch_Move(400, 300))
        COMTrans.RunSend(self.command.Touch_Move(400, 280))
        COMTrans.RunSend(self.command.Touch_Move(400, 260))
        COMTrans.RunSend(self.command.Touch_Move(400, 240))
        COMTrans.RunSend(self.command.Touch_Move(400, 220))
        COMTrans.RunSend(self.command.Touch_Move(400, 200))
        COMTrans.RunSend(self.command.Touch_Move(400, 180))
        COMTrans.RunSend(self.command.Touch_Up(400, 160))

    def DragUp(self):
        COMTrans.RunSend(self.command.Touch_Down(400, 160))
        COMTrans.RunSend(self.command.Touch_Move(400, 180))
        COMTrans.RunSend(self.command.Touch_Move(400, 200))
        COMTrans.RunSend(self.command.Touch_Move(400, 220))
        COMTrans.RunSend(self.command.Touch_Move(400, 240))
        COMTrans.RunSend(self.command.Touch_Move(400, 260))
        COMTrans.RunSend(self.command.Touch_Move(400, 280))
        COMTrans.RunSend(self.command.Touch_Move(400, 300))
        COMTrans.RunSend(self.command.Touch_Up(400, 320))

    #转换数据格式
    # def SendCommand(self):
    #     data = []
    #     buffer1 = (c_ubyte * (sizeof(self.newMDCCOMMAND)))()
    #     memset(buffer1, 0xFF, (sizeof(self.newMDCCOMMAND)))
    #     memmove(buffer1, byref(self.newMDCCOMMAND), (sizeof(self.newMDCCOMMAND)))
    #     for i in buffer1:
    #         data.append(i)
    #     print(data)
    #     print(len(data))
    #     #print(buffer1)
    #     return buffer1

if __name__ == "__main__":
    command = MDCCOMMAND()
    # command.SendCommand(command.Hardkey_Media_Down())
    # command.SendCommand(command.Hardkey_Media_Up())
    #
    # command.SendCommand(command.Volume_Left(2))
    # #sleep(0.5)
    # print("volune")
    # command.SendCommand(command.Volume_Right(3))

    command.Volume_Right()
    # command.SendCommand(command.ShortPressMediaKey())
    # command.SendCommand(command.ShortPressNextKey())
