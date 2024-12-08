package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	floar := 0
	firstBaseMentHit := []int{}
	for i, v := range data {
		if v == byte(40) {
			floar += 1
		} else {
			floar -= 1
		}
		if floar == -1 && len(firstBaseMentHit) == 0 {
			firstBaseMentHit = append(firstBaseMentHit, i)
		}
	}
	fmt.Println(floar)
	fmt.Println(firstBaseMentHit[0] + 1)
}
