package go_tour

import "fmt"

func main11()  {
	var i, j int = 1, 2
	k := 3  // 暗黙的な型宣言(varが不要)
	c, python, java := true, false, "no!"
	// var c, python, java = true, false, "no!" と同義
	// 関数の外ではvarが必須

	fmt.Println(i, j, k, c, python, java)
}