#!/usr/bin/env python3
# coding: utf-8

from pygame import mixer
import time, json

#initialize mixer
mixer.init()

#导入声音json列表
with open('/home/pi/robot_app/static/data/sound_list.json','r') as file:
    data = json.load(file)
sound_path = data
    
#播放音乐主函数
def play_sound(sound_source):
    sound = mixer.Sound(sound_source) #载入音乐
    sound_lenth = sound.get_length() #获取声音长度
    sound_lenth = round(sound_lenth,2) #保留小数点后两位
    print(sound_lenth)
    sound.play()
    time.sleep(sound_lenth)
    mixer.music.stop()

if __name__ == '__main__':
    while 1:
        '''
        for i in sound_path:
            play_sound(sound_path[i])#sound_path['sound1']
            print(sound_path[i])
            time.sleep(3)
        '''
    
