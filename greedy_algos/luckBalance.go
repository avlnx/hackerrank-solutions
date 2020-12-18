package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
	"sort"
)

// Complete the luckBalance function below.
func luckBalance(k int, contests [][]int) int {
	var maxLuck int = 0
	var importantContests []int
	maxLuck, importantContests = loseAllUnimportantContests(contests)
	sortByLuckFactorDesc(importantContests)
	return loseKImportantContests(importantContests, maxLuck, k)
}

func loseAllUnimportantContests(contests [][]int) (int, []int) {
	var maxLuck int = 0
	var importantContests []int
	for _, contest := range contests {
		luckFactor := contest[0]
		if contest[1] == 0 {
			// just lose if unimportant
			maxLuck += luckFactor
		} else {
			// important
			importantContests = append(importantContests, luckFactor)
		}
	}
	return maxLuck, importantContests
}

func sortByLuckFactorDesc(contests []int) {
	sort.Sort(sort.Reverse(sort.IntSlice(contests)))
}

func loseKImportantContests(contests []int, maxLuck int, k int) int {
	for _, luckFactor := range contests {
		if k > 0 {
			maxLuck += luckFactor
			k--
		} else {
			maxLuck -= luckFactor
		}
	}
	return maxLuck
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024 * 1024)

	nk := strings.Split(readLine(reader), " ")

	nTemp, err := strconv.ParseInt(nk[0], 10, 64)
	checkError(err)
	n := int(nTemp)

	kTemp, err := strconv.ParseInt(nk[1], 10, 64)
	checkError(err)
	k := int(kTemp)

	var contests [][]int
	for i := 0; i < int(n); i++ {
		contestsRowTemp := strings.Split(readLine(reader), " ")

		var contestsRow []int
		for _, contestsRowItem := range contestsRowTemp {
			contestsItemTemp, err := strconv.ParseInt(contestsRowItem, 10, 64)
			checkError(err)
			contestsItem := int(contestsItemTemp)
			contestsRow = append(contestsRow, contestsItem)
		}

		if len(contestsRow) != 2 {
			panic("Bad input")
		}

		contests = append(contests, contestsRow)
	}

	result := luckBalance(k, contests)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
