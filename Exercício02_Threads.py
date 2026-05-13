#2) Fazer uma aplicação que, na main, inicialize uma variável id, inteira e inicialize 5 variáveis
#inteiras para valores, crie um vetor de parâmetros, com o id como primeiro parâmetro e um
#vetor com os 5 valores recebidos. As variáveis que recebem os valores devem receber, cada
#uma delas, um valor aleatório de 1 a 100. Esses parâmetros devem ser preenchidos para 3
#chamadas de Threads. Faça 3 chamadas de Threads, passando os parâmetros e, cada Thread,
#deve calcular a soma de cada linha (Cada iteração do laço, para a soma deve ser seguido por
#um sleep de 0.2 segundos), ao final, deve-se imprimir a identificação da linha e o resultado da
#soma.

import random
import multiprocessing as mp
import time

def operacao(params):
    soma: int = 0 
    a1 = random.randint(1, 100)
    a2 = random.randint(1, 100)
    a3 = random.randint(1, 100)
    a4 = random.randint(1, 100)
    a5 = random.randint(1, 100)
    vetor = [a1, a2, a3, a4, a5]
    
    for i in range (0,5):
        soma += vetor[i]
        time.sleep(0.2)

    print('\n'+f"Thread #{params}: Soma = {soma}")
 
def main():
    id: int = 0
    params = [0]*3

    for id in range (3):
        params [id] = id

    with mp.Pool(processes=3) as pool:
        pool.map(operacao, params)

if __name__ == '__main__':
    main()