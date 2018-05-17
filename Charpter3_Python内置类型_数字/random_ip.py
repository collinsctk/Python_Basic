import random#导入random模块

#随机产生IP地址四个段落的数字
section1 = <学员填写>
section2 = <学员填写>
section3 = <学员填写>
section4 = <学员填写>

random_ip = str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4)
#要把数字转换成为字符串，并且拼接在一起！大家可以想象不转换的结果是什么？
print(random_ip)
#打印结果