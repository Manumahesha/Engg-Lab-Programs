package main

import "fmt"

func main() {
	myMap := make(map[string]int)
	myMap["apple"] = 1
	myMap["banana"] = 2
	myMap["orange"] = 3
	appleValue := myMap["apple"]
	bananaValue := myMap["banana"]
	fmt.Println("Value of apple:", appleValue)
	fmt.Println("Value of banana:", bananaValue)
	myMap["apple"] = 5
	fmt.Println("Updated value of apple:", myMap["apple"])
	delete(myMap, "orange")
	fmt.Println("Updated value of orange:", myMap)
	value, exists := myMap["banana"]
	if exists {
		fmt.Println("Value of banana:", value)
	} else {
		fmt.Println("Banan not found in the map")
	}
	for key, value := range myMap {
		fmt.Println("Key:", key, "value:", value)
		fmt.Println("Length of the map:", len(myMap))
	}
}

/*output
Value of apple: 1
Value of banana: 2
Updated value of apple: 5
Updated value of orange: map[apple:5 banana:2]
Value of banana: 2
Key: apple value: 5
Length of the map: 2
Key: banana value: 2
Length of the map: 2*/
