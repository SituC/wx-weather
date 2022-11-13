from wxpy import *

import requests



from apscheduler.schedulers.blocking import BlockingScheduler#定时框架

bot = Bot(cache_path=True)

# tuling = Tuling(api_key=你的api)#机器人api

def send_weather(location):

#准备url地址

    path ='https://v0.yiketianqi.com/api?unescape=1&version=v62&appid=41299442&appsecret=X2zK1mv5&ext=&cityid=&city=成都'

    response = requests.get(path)

    result = response.json()
    # print(result)

    # if result['error'] !=0:
    #     url = path 
    #     response = requests.get(url)
    #     result = response.json()

    str0 = '早上好呀宝宝，今天是%s %s，请查收今日份天气预报哦😘~\n' % (result['date'], result['week'])

    results = result

    # 取出数据字典

    data1 = results

    # 取出城市

    city = data1['city']

    str1 ='你的城市:    %s\n' % city

    pollution2 = data1['air_level']


    temperature_now = data1['tem']

    str2 ='当前温度:    %s℃\n' % temperature_now

    str3 ='最高温度:    %s℃\n' % data1['tem1']

    str4 ='最低温度:    %s℃\n' % data1['tem2']

    str5 ='空气指数:    %s\n' % pollution2

    # 取出pm2.5值

    pm25 = int(data1['air_pm25'])

    str6 ='Pm值      :    %s\n' % pm25

    wind = data1['win']

    str7 ='风向        :    %s\n' % wind

    weather = data1['wea']

    str8 ='天气        :    %s\n' % weather



    message = data1['zhishu']

    str9 ='穿衣        :    %s\n' % (message['chuanyi']['level'] + '，' + message['chuanyi']['tips'])

    str10 ='运动        :    %s\n' % data1['aqi']['yundong']

    str11 ='紫外线    :    %s\n' % (message['ziwaixian']['level'] + '，' + message['ziwaixian']['tips'])

    str12 ='小贴士    :    %s\n' % message['daisan']['tips']


    hours = data1['hours']
    Maxnums , Minnums = hours[0], hours[0]
    
    for i in range(len(hours)):
        if hours[i]['tem'] > Maxnums['tem']:
            Maxnums = hours[i]
        if hours[i]['tem'] < Minnums['tem']:
            Minnums = hours[i]

    str13 = '未来最低气温是在%s的%s℃\n' % (Minnums['hours'], Minnums['tem'])
    str14 = '未来最高气温是在%s的%s℃\n' % (Maxnums['hours'], Maxnums['tem'])
    str15 = '今天备课也要加油哦，新的一天再忙都要吃早餐🍕哦，么么哒😚'
    str = str0 + str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9 + str10 + str11 + str12 + str13 + str14 + str15

    return str

#好友列表

my_friends = []

# my_friends = bot.friends().search('Cherie')[0]
my_friends = bot.friends().search('宝宝', sex=FEMALE)[0]

print(my_friends)

#发送函数

def send_message():

    my_friends.send(send_weather('成都'))

#发送成功通知我

    bot.file_helper.send(send_weather('成都'))

    bot.file_helper.send('发送完毕')

#定时器

print('start')

# sched = BlockingScheduler()
sched = BlockingScheduler(timezone='Asia/Shanghai')
send_message()
# sched.add_job(send_message,'cron',month='1-12',day='1-31',hour=5,minute =30)

sched.start()