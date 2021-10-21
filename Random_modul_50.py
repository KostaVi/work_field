import random
date_day=random.randrange(1,29,1)
if len(str(date_day))==1:
	date_day= (str(0)+str(date_day))
date_month=random.randrange(1,13,1)
if len(str(date_month))==1:
	date_month= (str(0)+str(date_month))
date_year=random.randrange(1970,2001,1)
def date_random(date_day,date_month,date_year):
	return (str(date_day) + str(date_month) + str(date_year))
y=date_random(date_day,date_month,date_year)