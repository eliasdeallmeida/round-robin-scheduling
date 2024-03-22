class Processo:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remanescente = burst_time
     

def round_robin(processos, quantum):
    n = len(processos)
    tempo_espera = [0] * n
    tempo_retorno = [0] * n
    tempo = 0

    sequencia_execucao = [] 
    
    while True:
        done = True

        for i in range(n):
            p = processos[i]
          
            if p.remanescente > 0:
                done = False
                sequencia_execucao.append(p.pid)

                if p.remanescente > quantum:
                    tempo += quantum
                    p.remanescente -= quantum
                    tempo += 1
                else:
                    tempo += p.remanescente
                    tempo_espera[i] = tempo - p.burst_time
                    p.remanescente = 0
                    tempo += 1

        if done:
          break

    for i in range(n):
        tempo_retorno[i] = processos[i].burst_time + tempo_espera[i]

    print("Processos    Tempo de Espera   Tempo de Retorno")
    total_wt = 0
    total_tat = 0

    for i in range(len(processos)):
        total_wt = total_wt + tempo_espera[i]
        total_tat = total_tat + tempo_retorno[i]
        print(" ", i + 1, "\t\t", tempo_espera[i], "\t\t", tempo_retorno[i])

    print(f"\nTempo médio de espera = {total_wt /n}")
    print(f"Tempo médio de retorno = {total_tat / n} ")
    print(f"Tempo = {tempo}")
    vazao = len(processos) / tempo
    print("Vazão = %.5f processos por unidade de tempo" % vazao)
    print("Sequência de execução: ", sequencia_execucao)
  

if __name__ == '__main__':
    processos = [Processo(1, 10), Processo(2, 1), Processo(3, 5)]
    quantum = 4
    round_robin(processos, quantum)
