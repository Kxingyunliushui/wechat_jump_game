import random
import eventlet  # 导入eventlet这个模块
import time
import os


def jump(distance):
    press_time = distance * 1.35
    press_time = int(press_time)
    cmd = 'adb shell input swipe 745 1421 963 1421 ' + str(press_time)
    print(cmd)
    os.system(cmd)


eventlet.monkey_patch()  # 必须加这条代码
with eventlet.Timeout(20 * 60, False):  # 设置超时时间为2秒
    while True:
        jump(2)
        time.sleep(random.randint(5,15))





