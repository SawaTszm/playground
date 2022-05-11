package go_tour

import "fmt"

func add2(x, y int) int {  // 引数の型が同じ場合は最後以外を省略できる
	return x + y
}

func main6()  {
	fmt.Println(add2(42, 13))
}
