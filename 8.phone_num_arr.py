import re 

phone_num = "500-800-4623"
new_patt = re.compile("\d+")
new_num = new_patt.findall(phone_num)
print(new_num)

