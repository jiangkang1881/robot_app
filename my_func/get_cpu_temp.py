#!/usr/bin/python3
# coding:utf8
import time, json

def get_cpu_temp():
    # 获取CPU温度
    tmpFile = open('/sys/class/thermal/thermal_zone0/temp')
    cpu_temp_raw = tmpFile.read()
    tmpFile.close()
    cpu_temp = round(float(cpu_temp_raw) / 1000, 1)
    return cpu_temp

if __name__ == '__main__':
    
    while True:
        cpuTemp = get_cpu_temp()
        cpuTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        data = [cpuTemp, cpuTime]
      
        with open('/home/pi/robot_app/static/data/cpu_temp.json', 'w') as file:
            json.dump(data, file)

        print(data)
        time.sleep(3)
    
