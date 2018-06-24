实现功能：
通过串口，控制Radio执行软硬按键的操作；控制Canoe发送各种Can消息

该模块由4个文件构成：
1.__init__.py
2.Serial.py
3.COM_Config.json
4.Original_Command.py
5.Send_Command.py



文件1：空文件；
文件2：定义了串口通信功能；需在COM_Config.json文件中配置正确的COM以及波特率
文件3：配置COM口以及波特率
文件4：定义了命令格式以及基本的操作命令；
文件5：定义了两类: a.Commands类，定义实际操作的各种命令，由基本操作命令组织而成；
		  b.TestCases类，在该类里组织自己的TestCase，并他通过串口执行对应的Case

Change history
v1.0.0 	
	创建脚本
v1.1.0 	(2018.06.24)
	1.将Send_Command.py中Commands类移到Original_Command.py文件，并修改相关代码
	2.整合手机操作功能和Radio控制功能
	3.增加装饰器，如果step1失败，Case Fail，不会继续执行之后的case
	4.加入HTML Report 功能(已经美化，可以筛选Pass，Fail，Skip，Error的个数，需加入HTMLTestReportCN.py)；
	  注：需要在联网的情况下才能显示报告内容
	
	修改详情：
	
	D:\Install_SW\Python\Lib\unittest\case.py中新增如下代码：
	def Myskip(func):
		def RebackTest(self):
			if self._resultForDoCleanups.failures or self._resultForDoCleanups.errors:
				raise SkipTest("{} do not excute because {} is failed".format(func.__name__,self._resultForDoCleanups.failures[0][0]._testMethodName))
			func(self)
		return  RebackTest
		
	D:\Install_SW\Python\Lib\unittest\__init__.py中修改下面代码：

	__all__ = ['TestResult', 'TestCase', 'TestSuite',
			   'TextTestRunner', 'TestLoader', 'FunctionTestCase', 'main',
			   'defaultTestLoader', 'SkipTest', 'skip', 'skipIf', 'skipUnless',
			   'expectedFailure', 'TextTestResult', 'installHandler',
			   'registerResult', 'removeResult', 'removeHandler','Myskip']
	......
	from .case import (TestCase, FunctionTestCase, SkipTest, skip, skipIf,Myskip,
					   skipUnless, expectedFailure)
