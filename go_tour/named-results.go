package go_tour

import "fmt"

func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return  // naked return
}

func main8()  {
	fmt.Println(split(17))  // 7 10
	hoge, huga := split(17)  // hoge <- x, huga <- y
	fmt.Println(hoge)
	fmt.Println(huga)
}