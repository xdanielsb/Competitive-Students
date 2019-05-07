// version del programa en go lo mas eficiente que se logró

package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
  a := make([]byte,2E5) //se reserva espacio en memoria UNA VEZ EN TODO EL PROGRAMA (es rápido!)
	t, w := a[:1E5],a[1E5:] // no reserva espacio!
	for {
		var err1, err2 error
		t, err1 = reader.ReadBytes('\n') //al llamar a ReadString, se incluye el caracter '\n'
		w, err2 = reader.ReadBytes('\n')
		if err1 != nil || err2 != nil { // err1 == io.EOF || err2 == io.EOF
			break
		}
		fmt.Println(logic(t[:len(t)-1], w[:len(w)-1])) // se elimina el caracter '\n'
	}
}

func logic(t, w []byte) (count int) {
	for i := 0; i < len(t)-len(w)+1; i++ {
		if match(w, t[i:i+len(w)]) {
			count++
		}
	}
	return
}

func match(w, t []byte) bool { //len(w) == len(t)
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
