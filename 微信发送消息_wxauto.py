from wxauto import *

#使用WeChat()函数来获取微信的控制权限：
wx = WeChat()

'''
#使用GetSessionList()就会返回当前会话列表了：
sessionList = wx.GetSessionList()
if sessionList == '':
    print('没有登录！')
else:
    print(wx.GetSessionList())


#GetAllMessage()就可以获取当前窗口中加载的所有聊天记录：
msgs = wx.GetAllMessage
print(msgs)
for msg in msgs:
    print('%s : %s'%(msg[0],msg[1]))
'''

msg = '你好~'
who = '文件传输助手'
wx.ChatWith(who)
wx.SendMsg(msg)
