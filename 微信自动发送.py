from wxpy import *

#初始化一个机器人对象
bot = Bot(cache_path=True)
#向文件传输助手发送通知
bot.file_helper.send("登录成功！") #发送给文件传输助手

#查找Liva
my_friend = bot.friends().search('liva')[0]
#print(my_friend)
#发送消息
my_friend.send('Hello , My friend!')

#发送图片
#my_friend.send_image('D:/【100 - 项目】/【20230203 - FinReport】/BJ1.jpg')

#发送视频
#my_friend.send_video('')

#发送文件
#my_friend.send_file('')

# 获取所有好友[返回列表包含Chats对象(你的所有好友，包括自己)]
t0 = bot.friends(update=False)
# 查看自己好友数(除开自己)
print("我的好友数："+str(len(t0)-1))

# 获取所有微信群[返回列表包含Groups对象]
t1 = bot.groups(update=False)
# 查看微信群数(活跃的)
print("我的微信群聊数："+str(len(t1)))

# 获取所有关注的微信公众号[返回列表包含Chats对象]
t2 = bot.mps(update=False)
# 查看关注的微信公众号数
print("我关注的微信公众号数："+str(len(t2)))