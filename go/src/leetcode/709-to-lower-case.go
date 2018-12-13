package main

import "fmt"

func main() {
	fmt.Println(toLowerCase("AbCdEfG"))
}

func toLowerCase(str string) string {
	var result = ""
	for i := 0; i < len(str); i++ {
		if int(str[i]) < int('a') && (str[i] <= 'Z' && str[i] >= 'A' || str[i] <= 'z' && str[i] >= 'a') {
			result += string(int(str[i]) - int('A') + int('a'))
		} else {
			result += string(str[i])
		}
	}
	return result
}
