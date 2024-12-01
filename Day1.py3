
# Part 1

file = open('locationIDs.txt','r')
locationIDs = file.readlines()
summy = 0
left_list, right_list = [],[]

for i in range(len(locationIDs)):
	locationIDs[i] = locationIDs[i].strip('\n')

	left,right = locationIDs[i].split("   ")

	left_list.append(int(left))
	right_list.append(int(right))

	left_list.sort()
	right_list.sort()


differences = [abs(left_list[i]-right_list[i]) for i in range(len(left_list))]
summy = sum(differences)

# for i in range(len(left_list)):
# 	summy += abs(left_list[i]-right_list[i])


# print(summy)


# Part 2

similarity_score=0
for i in range(len(left_list)):
	cur = left_list[i]
	similarity_score += right_list.count(cur)*cur
print(similarity_score)