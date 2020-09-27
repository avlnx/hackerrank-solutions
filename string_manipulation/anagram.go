package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func bucketBytes(s string) map[byte]int {
	count := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		cur, found := count[s[i]]
		if !found {
			cur = 0
		}
		count[s[i]] = cur + 1
	}
	return count
}

// Complete the anagram function below.
func anagram(s string) int {
	sLen := len(s)
	if sLen%2 != 0 {
		return -1
	}
	first := bucketBytes(s[:sLen/2])
	sec := bucketBytes(s[sLen/2:])
	dups := 0
	for b, count := range first {
		secCount, found := sec[b]
		if !found {
			continue
		}
		dups += min(count, secCount)
	}
	return (sLen / 2) - dups
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024*1024)

	qTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	q := int32(qTemp)

	for qItr := 0; qItr < int(q); qItr++ {
		s := readLine(reader)

		result := anagram(s)

		fmt.Fprintf(writer, "%d\n", result)
	}

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
