#coding=utf-8
'''如果在此设置了用户名、密码，在启动WapFetion的时候会自动尝试进行登录。
填写完毕后重命名为config.py'''
mobile = '手机号'
password = '密码'
status = '在线状态' #在线：1；隐身：4；忙碌：2；离开：3
if len(mobile) == 11 and mobile.isdigit():
    data = 'm=%s&pass=%s&loginstatus=%s' % (mobile,password,status)
else:
    data = None