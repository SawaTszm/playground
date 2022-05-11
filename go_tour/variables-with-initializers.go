package go_tour

import "fmt"

var i, j int = 1, 2

func main10() {
	var c, python, java = true, false, "no!"  // 初期値がある場合型が省略可能(あんまりしたくはなさそう)
	fmt.Println(i, j, c, python, java)
}