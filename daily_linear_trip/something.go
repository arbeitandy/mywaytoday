package main

import (
	"fmt"
	"net/http"
)

func main() {
  var url string = "https://www.gizmochina.com/2021/06/23/redmi-gm-lu-weibing-stylishly-teases-the-redmi-k50-series"
	resp, err := http.Get(url)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer resp.Body.Close()
	fmt.Println(resp.Status)
}

// Output:
// 503 Service Temporarily Unavailable
// go run something.go
