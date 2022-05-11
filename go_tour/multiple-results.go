package go_tour

import "fmt"

func swap(x, y string) (string, string) {
	return y, x
}

func main7() {
	a, b := swap("hello", "world")
	fmt.Println(a, b)
}
