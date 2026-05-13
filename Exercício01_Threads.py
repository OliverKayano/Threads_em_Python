#1) Fazer uma aplicação que rode 5 Threads que cada uma delas receba um inteiro chamado id

#como parâmetro e imprima no console o texto “Thread #” + id. Antes de imprimir o valor, deve-
#se fazer um sleep de 0.5 segundos.

import multiprocessing as mp
import time

def processamento (id):
    print("Thread #", end='')
    time.sleep(0.5)
    print(id)

def main():
    i: int = 0
    params: int = [0]*5
    for i in range (5):
        params [i] = i
    with mp.Pool(processes=5) as pool:
        pool.map(processamento, params)

if __name__ == '__main__':
    main()