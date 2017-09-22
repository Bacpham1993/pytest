from datetime import time
def greeting_at(time_of_day):
	if time(5) < time_of_day < time(12):
		return 'morning'
	elif time(18) < time_of_day < time(21):
		return 'evening'
	else:
		return 'day'

