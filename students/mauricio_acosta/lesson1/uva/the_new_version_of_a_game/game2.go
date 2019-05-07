// version del programa en go usando una funcion especializada para la validacion
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	for {
		t, err1 := reader.ReadString('\n') //al llamar a ReadString, se incluye el caracter '\n'
		w, err2 := reader.ReadString('\n')
		if err1 != nil || err2 != nil { // err1 == io.EOF || err2 == io.EOF
			break
		}
		fmt.Println(logic(t[:len(t)-1], w[:len(w)-1])) // se elimina el caracter '\n'
	}
}

func logic(t, w string) (count int) {
	for i := 0; i < len(t)-len(w)+1; i++ {
		if match(w, t[i:i+len(w)]) {
			count++
		}
	}
	return
}

func match(w, t string) bool { //len(w) == len(t)
	flag := true
	for i, _ := range w {
		if w[i] == '?' {
			continue
		} else if w[i] != t[i] {
			flag = false
			break
		}
	}
	return flag
}
