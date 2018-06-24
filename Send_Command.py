#_*_coding:utf-8_*_

from time import sleep,strftime,localtime,time
#from Original_Command import *
#from appium import webdriver
import unittest
import HtmlTestRunner
import HTMLTestReportCN
import os

class AndroidPhoneTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'WTKDU16903013283'  # Honor8
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings$BluetoothSettingsActivity'
        desired_caps["unicodeKeyboard"] = 'True'
        desired_caps["resetKeyboard"] = 'True'

        global driver
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("setup")

    @classmethod
    def tearDownClass(self):
        os.system('adb shell ime set com.iflytek.inputmethod.FlyIME')  # 恢复为讯飞输入法
        self.driver.quit()

    def pair(self):

        #print("pair")

        # 判断蓝牙开关
        s = self.driver.find_element_by_id('android:id/switch_widget')
        if s.get_attribute('checked') == 'false':
            s.click()
        else:
            pass

        # 每次搜索到设备的id
        # self.driver.find_elements_by_id('androidhwext:id/preference_emui_content')

        sleep(5)  # 必须要足够的时间，手机才能发出请求

        global pairflag
        pairflag = 0
        j = 0
        while (j < 5 and pairflag == 0):
            i = 0
            while (i < 10):
                try:
                    self.driver.find_element_by_name('BUICK').click()
                    break
                except:
                    i = i + 1
                    if i == 10 and j == 4 :
                        raise "Can not find Device"
                    else:
                        continue
            ss = self.driver.find_elements_by_class_name("android.widget.Button")
            for ii in ss:
                if ii.text == u"知道了":
                    self.driver.find_element_by_name('知道了').click()
                    j = j + 1
                    if j == 5 :
                        raise "Can not connect Device"
                    break
                elif ii.text == u'配对':
                    s3 = self.driver.find_element_by_id(
                        'com.android.settings:id/phonebook_sharing_message_confirm_pin')
                    if s3.get_attribute('checked') == 'false':
                        s3.click()

                    sleep(1)

                    s2 = self.driver.find_element_by_name('配对')
                    s2.click()
                    pairflag = 1
                    break

    def unpair(self):
        self.driver.start_activity('com.android.settings', '.Settings$BluetoothSettingsActivity')

        s0 = self.driver.find_element_by_id("com.android.settings:id/konw_more")
        s0.click()

        s1 = self.driver.find_element_by_id("androidhwext:id/preference_emui_description_container")
        s1.click()

    def call(self):
        s0 = self.driver.start_activity('com.android.contacts', '.activities.DialtactsActivity')
        sleep(1)

        num1 = self.driver.find_element_by_name("1")
        num0 = self.driver.find_element_by_name("0")

        # Call 10010
        num1.click()
        num0.click()
        num0.click()
        num1.click()
        num0.click()

        # dial the call
        self.driver.find_element_by_id("com.android.contacts:id/dialButton").click()
        sleep(8)

        self.driver.find_element_by_id("com.android.incallui:id/endButton").click()

    def sendsms(self):
        # 定位SMS
        s0 = self.driver.start_activity('com.android.mms', '.ui.ComposeMessageActivity')
        sleep(1)

        # 编辑联系人
        s1 = self.driver.find_element_by_id("com.android.mms:id/recipients_editor")
        s1.send_keys("13262885325")

        # 返回，显示消息内容框
        # self.driver.press_keycode(4)

        # 编辑消息内容
        s2 = self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor")
        s2.send_keys(u'Hello World,你好，Appium')

        # 发送
        self.driver.find_element_by_id("com.android.mms:id/send_button_sms").click()

class TestCases(unittest.TestCase):
    '''
    需要执行的Case
    '''

    flg = False   #skip flag

    @classmethod
    def setUpClass(self):
        #self.SendCommand1 = Commands()

        # self.SendCommand1.InitHandShake()
        # print("ini command done")
        #
        # self.newphoneoperation = AndroidPhoneTests()
        # self.newphoneoperation.setUpClass()
        print("ini phone done")



    def cases(self):

        self.SendCommand1.PressHomekey()
        self.SendCommand1.PressHomekey()
        self.SendCommand1.DragLeft()
        sleep(2)
        self.SendCommand1.DragLeft()
        sleep(2)
        self.SendCommand1.DragRight()
        sleep(2)
        self.SendCommand1.TouchScreen(300, 110)
        sleep(2)
        self.SendCommand1.DragDown()
        sleep(2)
        self.SendCommand1.DragUp()
        self.SendCommand1.VolumeDecrease()
        self.SendCommand1.VolumePlus()
        self.SendCommand1.PressMediakey()
        self.SendCommand1.PressNextkey()
        self.SendCommand1.PressNextkey()
        self.SendCommand1.PressPreviouskey()
        self.SendCommand1.PressPreviouskey()
        self.SendCommand1.PressHomekey()
        self.SendCommand1.PressHomekey()
        self.SendCommand1.TouchScreen(120,100)

    @unittest.skipIf(flg,"Error")
    def test_001_Pair(self):

        #Radio进入蓝牙发现模式
        self.SendCommand1.TouchScreen(490, 110)  #Touch Phone icon
        self.SendCommand1.TouchScreen(720, 30)  # Touch bt setting
        self.SendCommand1.TouchScreen(400, 250)  # Touch Connect devices and enter into BT settings mode
        self.SendCommand1.TouchScreen(179, 110)  # Touch Connect devices and enter into pair mode

        self.newphoneoperation.pair()
        sleep(2)
        if pairflag:
            self.SendCommand1.TouchScreen(200, 430)  # Confirm on the Radio side
        else:
            assert "Pair Failed"

    @unittest.skipIf(flg, "Error")
    def test_002_UnpairR(self):

        #Radio端取消连接，取消配对
        self.SendCommand1.PressHomekey()
        self.SendCommand1.PressHomekey()

        self.SendCommand1.TouchScreen(490, 110)  #Touch Phone
        self.SendCommand1.TouchScreen(720, 30)  # Touch Phone
        self.SendCommand1.TouchScreen(760, 210)  # Disconnect
        self.SendCommand1.TouchScreen(200, 430)  # Confirm Disconnect
        self.SendCommand1.TouchScreen(760, 310)  # Unpair

        #self.newphoneoperation.pair()

    #@unittest.Myskip
    @unittest.skipIf(flg, "Error")
    def test_UnpairP(self):

        #手机端取消连接，Radio取消配对
        self.SendCommand1.PressHomekey()
        self.SendCommand1.PressHomekey()
        self.newphoneoperation.unpair()
        sleep(8)
        self.SendCommand1.TouchScreen(490, 110)  # Touch Phone icon
        self.SendCommand1.TouchScreen(720, 30)  # Touch bt setting
        self.SendCommand1.TouchScreen(400, 250)  # Touch Connect devices and enter into BT settings mode
        self.SendCommand1.TouchScreen(760, 310)  # Unpair

    @unittest.skipIf(flg, "Error")
    def test_003_Test(self):
        print("NOK")

class TestOne(unittest.TestCase):

    def test_001(self):
        print("pass")

        raise AssertionError("NOK")

    @unittest.Myskip
    def test_002(self):

        print("pass")
        raise AssertionError("NOK")

    @unittest.Myskip
    def test_003(self):

        # if self._resultForDoCleanups.failures or self._resultForDoCleanups.errors:
        #     raise unittest.SkipTest("{} do not excute because {} is failed".format(self._testMethodName,self._resultForDoCleanups.failures[0][0]._testMethodName))
        print("pass")

class TestTwo(unittest.TestCase):

    def test_001(self):
        print("pass")
        raise AssertionError("NOK")

    @unittest.Myskip
    def test_002(self):
        print("excute test3")



if __name__ == '__main__':

    #  AddTest 方法
    suite = unittest.TestSuite()
    #suite.addTest(TestCases('test_001_Pair'))
    #suite.addTest(TestCases('test_002_UnpairR'))

    #suite.addTest(TestCases('test_004_Test'))
    #suite.addTest(TestCases('test_003_Test'))

    suite.addTest(TestOne('test_001'))
    suite.addTest(TestOne('test_002'))
    suite.addTest(TestOne('test_003'))
    suite.addTest(TestTwo('test_001'))
    suite.addTest(TestTwo('test_002'))

    #创建Report文件夹
    path =os.getcwd()+ '\\Report\\'
    isExists = os.path.exists(path)
    if not isExists:
        # 不存在，则创建目录
        os.makedirs(path)

    #timestamp = strftime('%Y-%m-%d-%H-%M-%S', localtime(time()))

    timestamp = strftime('%Y-%m-%d-%H-%M-%S', localtime(time()))

    with open(path+'TestReport_' + timestamp + '.html', 'wb') as fp:
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,title=u'自动化测试报告',
            tester=u"Zhang Jiankai") # 测试人员名字，不传默认为QA
        runner.run(suite)


    # suite = unittest.defaultTestLoader.discover(start_dir=r'D:\Code\Python\MessagelatenciesTest\SerialCOM_v1.0.0',pattern='test_00*.py')
    # print(suite)
    # timestamp = strftime('%Y-%m-%d-%H-%M-%S', localtime(time()))
    #
    # with open ('TestReport_' + timestamp + '.html', 'wb') as fb:
    #     runner = HTMLTestReportCN.HTMLTestRunner(stream=fb, title='Report_title',description='Report_description')
    # runner.run(suite)
    # fb.close()
    #sleep(2)  # 设置睡眠时间，等待测试报告生成完毕


    # suite = unittest.TestSuite()
    # suite.addTest(AndroidPhoneTests('test_pair'))