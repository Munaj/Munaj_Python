import re
mail = "jan@onremove_thiset.pl"
search = "remove_this"
res = re.search(search,mail)
if res:
    print(mail.replace(search, ""))
else:
    print("couldn't find match")





