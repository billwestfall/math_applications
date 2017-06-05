from datetime import strptime

time_str = '2012/01/01 12:32:11'

dt = datetime.strptime(time_str, '%Y/%m/%d %H:%M:%S')

print(dt)
