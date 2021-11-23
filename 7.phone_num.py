import re
phone_num = "345-03-02"

new_num = re.sub("-","",phone_num)
print(new_num)
