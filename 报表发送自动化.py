# 导入工具包
from wxauto import WeChat
import time


# 给单人发送消息
#to = "文件传输助手"  # 要发送的人
to = "lilily----"   #要发送的人
msg = "今天的日报请查收："  # 要发送的消息
file = "D:/Temp/大屏布局 V2.0.xlsx"  # 要发送的文件
wx = WeChat()  # 获取当前微信客户端
wx.Search(to)  # 打开聊天窗口
wx.SendMsg(msg)  # 发送消息
wx.SendFiles(file)  # 发送文件
print("发送结束！")

'''
# 给多人发送消息
to_names = ["文件传输助手", "运营组", "产品组"]  # 要发送的人或群
file = "D:\Documents\Desktop\日报.xlsx"  # 要发送的文件
msg = "今天的日报请查收："  # 要发送的消息
wx = WeChat()  # 获取当前微信客户端
for to in to_names:
    time.sleep(3)  # 等待3秒
    wx.Search(to)  # 打开聊天窗口
    wx.SendMsg(msg)  # 发送消息
    wx.SendFiles(file)  # 发送文件
print("发送结束！")
'''
