package main

import (
	"fmt"
	"math"
)

type Shape interface {
	Area() float64
}
type Circle struct {
	radius float64
}

func (c Circle) Area() float64 {
	return math.Pi * c.radius * c.radius
}

type Rectangle struct {
	width  float64
	hieght float64
}

func (r Rectangle) Area() float64 {
	return r.width * r.hieght
}
func PrintArea(s Shape) {
	fmt.Printf("Area:%0.2f\n", s.Area())
}
func main() {
	circle := Circle{radius: 5}
	rectangle := Rectangle{width: 4, hieght: 6}
	PrintArea(circle)
	PrintArea(rectangle)
}

//output
//Area:78.54
//Area:24.00
