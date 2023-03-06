import itchat

itchat.auto_login(hotReload=True) #hotReload= True可以暂存登录状态，退出后一定时间内重启不用再次扫码登录。
friends = itchat.get_friends(update=True)[0:]
#print(friends)
result = itchat.search_friends(name='莉�')

print(result)
user_name = itchat.search_friends(name='莉�')
#itchat.send_msg('微信测试',toUserName=user_name)
itchat.send(msg='测试微信',toUserName='@60873d717b5daf3dc42a2b6e8fc186d62f7c73255e1c59d291c59338b2aa7fbf')
'''
#发送消息给特定好友
itchat.auto_login(hotReload=True)
friends_list =itchat.get_friends(update=True)
users =itchat.search_friends(name=u'liva')
print(users)
userName = users[0]["lilily----"]
itchat.send('正在测试微信机器人...' ,toUserName = userName)

    'user_info = itchat.search_friends(name="lilily----")
'''
'''
# 发送消息
def send_msg():
    user_info = itchat.search_friends(wechatAccount='lilily----')
    print(user_info)
    if len(user_info) > 0:
        print("Yes")
        user_name = user_info[0]['UserName']
        print(user_name)
        itchat.send_msg('微信测试',toUserName=user_name)

if __name__ == '__main__':
   send_msg()
'''