#4) No Sistema Operacional Linux, o comando para realizar uma operação de ping com 10
#iterações é ping -4 -c 10 <servidor> e no Sistema Operacional Windows, o comando para a
#mesma função é ping -4 -n 10 <servidor>. Fazer uma aplicação Python que rode 3 Threads,
#sendo que a Thread deve identificar o SO para rodar o comando certo, fazendo operação de
#ping para os servidores UOL (www.uol.com.br), Terra (www.terra.com.br) e Google
#(www.google.com.br). Cada thread deve ler a saída do ping imprimindo, a cada iteração, o
#nome do servidor (usar fixo: UOL, Terra ou Google) e o tempo daquela iteração. Ao fim, deve-
#se exibir o nome do servidor (usar fixo: UOL, Terra ou Google) e o tempo médio obtido pela
#operação. Outros Sistemas Operacionais devem ser descartados.

import platform
import subprocess
import multiprocessing as mp

def os_name ():
   system: str = ''
   system = platform.system()

   return(system)

def le_processo(id, processo):

   vetor_processo: str = []
   vetor_saida: str = []
   saida: str = ''
   linha: str = ' '
   c: int = 0

   vetor_processo = processo.split(' ')
   saida = subprocess.Popen(vetor_processo, stdout = subprocess.PIPE)
   linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')

   while (linha != ''):
      linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')

      if ('avg' in linha):

         vetor_saida = linha.replace(' ', '/').replace('\n','').split('/')

         for c in range (0, len(vetor_saida),1):
            if vetor_saida [c] == 'avg':
               print(id+': '+vetor_saida[c]+'/'+ vetor_saida[c+5], vetor_saida[c+8])


      if ('Mdia' in linha):
         vetor_saida = linha.replace('\r', ' ').split(' ')

         for c in range (0, len(vetor_saida), 1):
            if (vetor_saida [c] == 'Mdia'):
              print(id + ': ' +vetor_saida [c], vetor_saida [c+1], vetor_saida [c+2])

def main():

   os: str = ''
   processo = [] 

   os = os_name()

   if (os == 'Linux') :
      processo.append(["Google", "ping -4 -c 10 www.google.com.br"])
      processo.append(["UOL", "ping -4 -c 10 www.uol.com.br"])
      processo.append(["Terra", "ping -4 -c 10 www.terra.com.br"])

   if (os == 'Windows') :
      processo.append(["Google", "ping -4 -n 10 www.google.com.br"])
      processo.append(["UOL", "ping -4 -n 10 www.uol.com.br"])
      processo.append(["Terra", "ping -4 -n 10 www.terra.com.br"])

   with mp.Pool(processes=3) as pool:
         pool.starmap(le_processo, processo)

if __name__ == '__main__':
   main()