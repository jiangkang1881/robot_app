from flask import Flask, render_template, request, Response
from my_func import play_music
import os, json, serial

ser = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = 1)
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
    elif btn_state == 'sound3': 
        play_music.play_sound(play_music.sound_path['sound3'])
    elif btn_state == 'sound4': 
        s = '#12P1800#32P1500T1000D800\r\n'
        ser.write(s.encode('utf-8'))#写入串口指令
    elif btn_state == 'sound5': 
        s = '#12P1000#32P1000T1000D800\r\n'
        ser.write(s.encode('utf-8'))#写入串口指令
    else:
        pass
    return render_template('index.html')
        
@app.route('/temp',methods=["GET", "POST"])
def draw_stone():
    # Reading data back
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
