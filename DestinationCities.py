def DestinationCity(paths):
	"""
	You are given the array paths, where paths[i] = [cityAi, cityBi] means 
	there exists a direct path going from cityAi to cityBi. Return the destination city, 
	that is, the city without any path outgoing to another city.
	It is guaranteed that the graph of paths forms a line without any loop, 
	therefore, there will be exactly one destination city.
	Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
	Output: "Sao Paulo" 
	Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. 
	Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

	Input: paths = [["B","C"],["D","B"],["C","A"]]
	Output: "A"
	Explanation: All possible trips are: 
	"D" -> "B" -> "C" -> "A". 
	"B" -> "C" -> "A". 
	"C" -> "A". 
	"A". 
	Clearly the destination city is "A".
	Input: paths = [["A","Z"]]
	Output: "Z"
	"""
	#create sets to hold the cities in the start city, and end city
	start_cities, end_cities = set(), set()

	#entering the values to their respective places, i.e path[i][0] - start, path[i][1] - end
	for start, end in paths:
		start_cities.add(start)
		end_cities.add(end)

	#if value is in the end_cities, but not in the start, then it is the destination
	for end in end_cities:
		if end not in start_cities:
			return end


