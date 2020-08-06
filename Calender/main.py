# code with <3 by Absera

# Interview Question
# The program takes two calenders two people as inputs and return free time slots
# that the two people can meet
# There are also boundaries of time for each calenders

# for example: sample inputs:
	# person1sechedule = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
	# person1boundary = ["1:00", "11:00"]
	# person2schedule = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
	# person2boundary = ["2:00", "12:00"]

	# sample output:
		#  output = [[1130, 1200], [1500, 1600], [1800, 1830]]
		# which means the two people can meet between the times above



def change_to_num(time):
	x,y = time.split(":")
	k = x + y
	k = int(k)

	return k

def get_free_time(schedule, boundary):
	# schedule = [[900, 1030], [1200, 1300], [1600, 1800]]
	# boundary = [900, 2000]
	free_time = []
	for i, j in zip(schedule, schedule):
		i_index = schedule.index(i)
		# j_index = i_index + 1 if i_index < len(schedule)-1 else -1
		if i_index < len(schedule) - 1:
			j_index = i_index + 1
			if not schedule[i_index][1] == schedule[j_index][0]:
				free_time.append([schedule[i_index][1], schedule[j_index][0]])
		else:
			j_index = 1
			if boundary[1] > schedule[i_index][1]:
				free_time.append([schedule[i_index][1], boundary[1]])

	return free_time

def merge_free_times(time1, time2):
	# time1 = [[1130, 1230], [1500, 1600], [1700, 1830]]
	# time2 = [[1030, 1200], [1300, 1600]]
	output = []

	for i, j in zip(time1, time2):
		output.append(sorted(sorted(i) + sorted(j)))

	return sorted(output)

def give_output(merged_free_time):
	for i in merged_free_time:
		i.pop(0)
		i.pop(-1)

	return merged_free_time




s1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
s1_boundary = ["9:00", "20:00"]
s2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
s2_boundary = ["10:00", "18:30"]

# s1 = [["1:00", "2:30"], ["6:00", "9:00"]]
# s1_boundary = ["1:00", "11:00"]
# s2 = [["2:00", "3:30"], ["7:00", "10:30"]]
# s2_boundary = ["2:00", "12:00"]


s1_to_num = [[change_to_num(i[0]), change_to_num(i[1])] for i in s1 ]
s1_boundary_to_num = [change_to_num(s1_boundary[0]), change_to_num(s1_boundary[1])]
s1_free_time = get_free_time(s1_to_num, s1_boundary_to_num)

s2_to_num = [[change_to_num(i[0]), change_to_num(i[1])] for i in s2 ]
s2_boundary_to_num = [change_to_num(s2_boundary[0]), change_to_num(s2_boundary[1])]
s2_free_time = get_free_time(s2_to_num, s2_boundary_to_num)

# print(s2_free_time)
merged_free_time = merge_free_times(s1_free_time, s2_free_time)
output = give_output(merged_free_time)
print(output)
