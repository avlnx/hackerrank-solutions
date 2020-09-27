package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

/*
 * Complete the timeConversion function below.
 */
func timeConversion(s string) string {
	/*
	 * Write your code here.
	 */
	// 12:00:00AM => 00:00:00
	// 12:00:00PM => 12:00:00
	hour, _ := strconv.Atoi(s[0:2])
	hour = hour % 12
	mapToIntDiff := map[string]int{"AM": 0, "PM": 12}
	amPm := s[8:10]
	hour = (hour + mapToIntDiff[amPm]) % 24
	rest := s[2:8]
	return fmt.Sprintf("%02s%s", strconv.Itoa(hour), rest)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	outputFile, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer outputFile.Close()

	writer := bufio.NewWriterSize(outputFile, 1024*1024)

	s := readLine(reader)

	result := timeConversion(s)

	fmt.Fprintf(writer, "%s\n", result)

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
