#!/usr/bin/python
# coding=UTF-8
from flask import Flask, render_template, request, Response
from my_func import play_music
import os, json, serial

ser = serial.Serial('/dev/ttyS0', baudrate = 115200, timeout = 1)
#serial communication


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setting')
def setting():
    return render_template('setting.html')

@app.route('/<btn_state>')
def btn_switch(btn_state):
    if btn_state == 'sound1': 
        play_music.play_sound(play_music.sound_path['sound1'])
    elif btn_state == 'sound2': 
        play_music.play_sound(play_music.sound_path['sound2'])
    elif btn_state.find("#") == True:
        print(btn_state)
        ser.write(btn_state.encode('utf-8'))#写入串口指令
    elif btn_state == 'sound4': 
        s = '{#000P0500T1000!#023P0900T1000!}'
        ser.write(s.encode('utf-8'))#写入串口指令
    elif btn_state == 'sound5': 
        s = '{#000P1500T1000!#023P2000T1000!}'
        ser.write(s.encode('utf-8'))#写入串口指令
    else:
        pass
    return render_template('index.html')

@app.route('/play/',methods=["POST"])
def play():
        code = request.form["instruction"]#获取前端指令
        ser.write(code.encode('utf-8'))#写入串口指令
        return code
        
@app.route('/temp',methods=["GET", "POST"])
def draw_stone():
    # 读取json格式的cpu温度
    with open('/home/pi/robot_app/static/data/cpu_temp.json', 'r') as f:
        data = json.load(f)
    return Response(json.dumps(data), mimetype='application/json')#更新前端温度信息
    
@app.route('/poweroff')
def poweroff():
    os.system("sudo poweroff")

@app.route('/reboot')
def reboot():
    os.system("sudo reboot")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)

