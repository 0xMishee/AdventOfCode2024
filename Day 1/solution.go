package main

import (
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func getLists(path string) ([]int, []int) {
	inputData, err := os.ReadFile(path)
	check(err)

	var leftList, rightList []int

	lines := strings.Split(string(inputData), "\n")

	for _, line := range lines {
		newLine := strings.Fields(line)

		leftValue, err := strconv.Atoi(newLine[0])
		check(err)

		rightValue, err := strconv.Atoi(newLine[1])
		check(err)

		rightList = append(rightList, rightValue)
		leftList = append(leftList, leftValue)
	}

	sort.Slice(leftList, func(i, j int) bool {
		return leftList[i] < leftList[j]
	})

	sort.Slice(rightList, func(i, j int) bool {
		return rightList[i] < rightList[j]
	})

	return leftList, rightList
}

func totalDistance(rightList, leftList []int) int {
	var totalDistanceScore int

	for i := 0; i < len(rightList); i++ {
		totalDistanceScore += int(math.Abs(float64(rightList[i] - leftList[i])))
	}
	return totalDistanceScore
}

func similairScore(leftList, rightList []int) int {
	var similairScore int

	count := make(map[int]int)

	for _, value := range leftList {
		count[value]++
	}

	for _, value := range rightList {
		count := count[value]
		similairScore += value * count
	}

	return similairScore
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	inputPath := "input.txt"

	leftList, rightList := getLists(inputPath)

	totalDistance := totalDistance(rightList, leftList)
	similairScore := similairScore(leftList, rightList)

	fmt.Printf("Total distance: %d\n", totalDistance)
	fmt.Printf("Similair score: %d\n", similairScore)
}
