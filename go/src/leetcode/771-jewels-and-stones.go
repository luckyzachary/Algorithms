package leetcode

import "fmt"

func main() {
	fmt.Println(numJewelsInStones("aA", "aAAbbbb"))
	x := 1 << 2
	y := 1 << 4
	z := x & y
	fmt.Println(z)
	var a int = 'a' - 'A'
	fmt.Println(a)
}

func numJewelsInStones(J string, S string) int {
	var j uint64 = 0
	for i := 0; i < len(J); i++ {
		j |= 1 << (J[i] - 'A')
	}
	count := 0
	for i := 0; i < len(S); i++ {
		if 0 != j&(1<<(S[i]-'A')) {
			count++
		}
	}
	return count
}
