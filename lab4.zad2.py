from datetime import *

today_date = date.today()
diff = timedelta(days=5)

past = today_date - diff
future = today_date + diff
print(past)
print(future)