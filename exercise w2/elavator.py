def elevator_trips (people_weight, people_floors, elevator_floors, max_people, max_weight):
	count=0
	current_weight=0
	current_people=0
	curent_state=[]
	strfl=0
	if len(people_weight)==0 or len(people_floors)==0:
		return 0
	for i in range(len(people_weight)):
		temp=current_weight+people_weight[i]
		count_lifts=0
		if current_weight<max_weight and current_people<max_people and temp<=max_weight:
			current_people+=1
			current_weight=temp
			curent_state.append((people_floors[i],people_weight[i]))
		else:
			curent_state=sorted(curent_state)
			print(curent_state)
			for j in curent_state:
				if j[0]>strfl:
					strfl=j[0]
					count+=1
			count+=1
			strfl=0
			current_weight=0
			current_weight=people_weight[i]
			current_people=1
			curent_state=[]
			curent_state.append((people_floors[i],people_weight[i]))
	strfl=0
	for i in curent_state:
		if i[0]>strfl:
			strfl=i[0]
			count+=1
	count+=1



	return count


print(elevator_trips([], [1,2,3], 5, 2, 200))
