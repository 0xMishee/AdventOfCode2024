package main

import (
	"fmt"
	"os"
	"strings"
)

// Check if slice is made out of decreasing numbers.
func decreasing(row []int) bool {
	for i := 0; i < len(row)-1; i++ {
		diff := row[i+1] - row[i]
		if diff < 1 || diff > 3 {
			return false
		}
	}
	return true
}

// Check if slice is made out of increasing numbers.
func increasing(row []int) bool {
	for i := 0; i < len(row)-1; i++ {
		diff := row[i] - row[i+1]
		if diff < 1 || diff > 3 {
			return false
		}
	}
	return true
}

// Check if either condition are true.
func safeCheck(row []int) bool {
	return decreasing(row) || increasing(row)
}

// Transform String of seperated ints to type "int array/slice".
func stringToIntList(row string) []int {

	digitsStr := strings.Fields(row)
	digits := make([]int, len(digitsStr))
	for i, s := range digitsStr {
		fmt.Sscanf(s, "%d", &digits[i])
	}
	return digits
}

func safeReportCountFunc(row string) int {

	var safeStatus int

	digits := stringToIntList(row)
	if safeCheck(digits) {
		safeStatus++
	}

	return safeStatus

}

// Check if either condition are true, but with fault tolerance.
func safeReportCountFaultToleranceFunc(row string) int {

	digits := stringToIntList(row)

	if safeCheck(digits) {
		return 1
	}

	for i := 0; i < len(digits); i++ {

		temp := make([]int, len(digits))
		copy(temp, digits)

		faultToleratedReport := append(temp[:i], temp[i+1:]...)
		if safeCheck(faultToleratedReport) {
			return 1
		}
	}
	return 0
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	var safeReportCount int
	var safeReportCountFaultTolerance int

	levels, err := os.ReadFile("input.txt")
	check(err)

	lines := strings.Split(string(levels), "\n")

	for _, row := range lines {
		safeReportCount += safeReportCountFunc(row)
		safeReportCountFaultTolerance += safeReportCountFaultToleranceFunc(row)
	}

	fmt.Println("Safe Report Count: ", safeReportCount)
	fmt.Println("Safe Report Count Fault Tolerance: ", safeReportCountFaultTolerance)

}
