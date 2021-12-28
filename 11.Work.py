import re
x = "Dell 4/256"

ssd128z,ssd128s = 90,63
ssd256z,ssd256s = 135,95
ssd512z,ssd512s = 250,175
hdd320z,hdd320s = 50,35
hdd500z,hdd500s = 70,49
ram_4gbz,ram_4gbs = 80,56
ram_8gbz,ram_8gbs = 160,112

x256 = 1399
x128 = x256 - ssd256s + ssd128z
x512 = x256 - ssd256s + ssd512z + 50

ram_ssd = ["4/128","4/256","4/512","8/128","8/256","8/512","16/128","16/256","16/512"]
prices = [x128-ram_4gbs,x128,x128-(2*ram_4gbs)+(2*ram_8gbz)+50,
            x256-ram_4gbs,x256,x256-(2*ram_4gbs)+(2*ram_8gbz)+50,
            x512-ram_4gbs+50,x512,x512-(2*ram_4gbs)+(2*ram_8gbz)+100]

i=0
