import random
import eventlet  # 导入eventlet这个模块
import time
import os


def jump(distance):
    press_time = distance * 1.35
    press_time = int(press_time)
    cmd = 'adb shell input swipe 745 1421 963 1421 ' + str(press_time)
    now = int(time.time())
    rate = (now - start_time)/(16 * 60)
    time_now = time.localtime(now)
    timestr = time.strftime("%Y-%m-%d %H:%M:%S", time_now)
    strstr = "cmd=%s, time=%s, rate:%2f%%" % (cmd, timestr, rate)
    print(strstr)

    os.system(cmd)

start_time = int(time.time())
eventlet.monkey_patch()  # 必须加这条代码
with eventlet.Timeout(16 * 60, False):  # 设置超时时间为2秒
    while True:
        jump(2)
        time.sleep(random.randint(5,15))





