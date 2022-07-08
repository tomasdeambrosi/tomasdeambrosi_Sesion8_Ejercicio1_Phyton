'''En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis 
dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.'''

f = open('fichero.txt', 'w')
f.write('Primer acceso: archivo creado\n')
f.close

f = open('fichero.txt', 'a+')
f.write('\nSegundo acceo: hola mundo!')
f.close
