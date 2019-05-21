    ´´´ 
    # Abrindo o arquivo de texto a ser lido.
    abrindoarq = open('arquivo.txt','r')
    # aplicando o metodo read para ler o arquivo.
    metodoread = abrindoarq.read()
    # aplicando o método split que torna o arquivo de texto em um vetor e armazendao ele em uma variavel.
    splited = metodoread.split(" ")
    #criando uma variavel executar que servirá para laço while que antecede a execução dos procedimentos.
    executar = 1
    #criando uma variavel para armazenar o tempo total de execução do processo.
    exucacaotoatal = 0
    #criando uma variavel para armazenar o tempo total de execução da cpu.
    totaldacpu = 0
    #criando uma variavel para armazenar o tempo total de execução da  es.
    totales = 0
    #criando uma variavel para armazenar o tempo medio de execução dos processos.
    tempomedio = 0
    #criando um vetor onde será armazenado os processos.
    processo = [''] * 8
    #criando um vetor onde será armazenado os tipos de processos.
    tipodeprocesso = [''] * 8
    #criando um vetor onde será armazenado o tempo de execução dos processos.
    tempo = [0] * 8
    #criando um variavel para ordenação dos  processos.
    proxlivre1 = 0
    #criando um variavel para ordenação dos  tipos de processos.
    proxlivre =0
    #criando um variavel para ordenação do tempo.
    proxlivre2 = 0
    # importando um biblioteca para utilizar o método sleep na execução.
    import time
    #importando outra biblioteca que permite limpar a tela do " TERMINAL " durante a execução do programa. Para otimizar
    #o processo de visualização do programa oriento a executar-lo no terminal, pois o metodo disposto por essa biblioteca
    # só funciona lá.
    import os

    # aplicando um laço for tendo como parametro o vetor splited.
    for i in range(len(splited)):
    # utilizando a extrutura de condição if para comparar as informações presentes no vetor com aquelas que desejamos extrair.
      if splited[i] == "p1" or splited[i] == "p2" or splited[i] == "p3" or splited[i] == "p4":
    # caso essas informações sejam validades ocorre um procedimento de comparação para avaliar se a posição no vetor processo
    # esta livre.
          if processo[proxlivre1] == '':
    #caso esteja o valor é inserido.
             processo[proxlivre1] = splited[i]
    # a variavel proximo livre garante que o valor será inserido na proxima posição livre no vetor processo
             proxlivre1 = proxlivre1 + 1
          else:
    # se não for encontrando um valor equivalente nas comparações ou se não houver mais nenhunma posição livre no vetor processo
    # o else executara um break no laço, e isso impedirá que haja erro de indexação.
           break
    # o mesmo processo realizado acima é novamente realizado abaixo nesta estrutura de decisão, mas desta vé o intuito é encontrar elementos equivalentes aos tipos
    # de processos existentes na cpu
      if splited[i] == "cpu" or splited[i] == "es" and tipodeprocesso[proxlivre] == '':
        tipodeprocesso[proxlivre] = splited[i]
        proxlivre += 1

    # os mesmos dois processos realizados acima são realizados mais três vezes abaixo, no entanto, nestas vezes o objetivo e identificar
    # e armazenar os dados do tipo int que representam os tempos de processo.
      if splited[i] == '2' :
        tempo[proxlivre2] = 2
        proxlivre2 = proxlivre2 + 1

      if splited[i] == '3':
        tempo[proxlivre2] = 3
        proxlivre2 = proxlivre2 + 1

      if splited[i] == '4':
        tempo[proxlivre2] = 4
        proxlivre2 = proxlivre2 + 1

    print(processo)
    print(tempo)
    print(tipodeprocesso)

    executar =1
    # aplicando o laço while para proporcional um menu de execução que solicitara permissão do usuario para executar o programa.
    while executar == 1:
        print("Tecle 1 para executar o processo")
        receber = int(input())
        if receber == 1:
    # caso ele digite a opção correta o laço será quebrado, caso contrario a tela exibira uma mensagem de erro
    # e solicitará novamente o comando.
         break
        else:
            print("-" * 20)
            print("Opção invalida tente novamente")
            print("-" * 20)

    #caso o laço while seja quebrado, então será dado inicio a um laço for determinado pelo numero de processos presentes
    #no vetor processo.
    for i in range(len(processo)):
    # a variavel x tem como função parametizar o laço while que proporcionará repetidos prints de tela até que a posição
    # do vetor tempo chegue a zero.
             x = 1
    # a variavel tempoestimado tem como uma função armazenar a posição do vetor tempo antes da execução do laço while de modo que seu
    # valor não seja alterado no decorrer do processo.
             tempoestimado = tempo[i]
    # no final de cada print constara o valor presente na posição do vetor em questão, essa posição varia de acordo com as voltas
    # do laço for.
             while x:
                print('\n')
                print("Simulador SO Monotarefa")
                print("Executanto o processo: %s" %(processo[i]))
                print("Tipo do processo: %s" %(tipodeprocesso[i]))
                print("Tempo estimado de execução: %d" %(tempoestimado))
                print("Tempo restante: %d" %(tempo[i]))
                print('\n')
    # metodo sleep impregado para causar um delay proposital da execução do processo
                time.sleep(1)
                tempo[i] = tempo[i] - 1
    # O metodo utilizado para limpar a tela durante o processo de execução, recomendo novamente que o script seja executado
    # no terminal
                os.system('cls')
    # Quando a posição do vetor tempo chega a zero e o while sofre um break e uma volta no laço for é executada.
                if tempo[i] == 0:
                    break
    # a variavel execucaototal guardará as informações presentes na variavel tempo estimado acomulando o tempo total de execução
    # no final do processo.
             exucacaotoatal = exucacaotoatal + tempoestimado
    # Toda vez que o laço se deparar com um tipo de processo "cpu", ele irá armazenar o tempo de execução desse processo na variavel
    # totaldacpu, acumalando os valores através da variavel tempoestimado
             if tipodeprocesso[i] == "cpu":

                    totaldacpu = totaldacpu + tempoestimado
             else:
    # caso a estrutura identifique que não se trata de um processo " cpu " ela irá armazenar automaticamente o tempo de execução
    # na variavel totales que representa o tempo de execução total do tipo de processo es, lembrando que no vertor tipo de processo
    # só possui dois tipo " cpu " e " es ".
                    totales = totales + tempoestimado

    # por fim a variavel tempo médio tratará de dividir o tempo total de execução pelo numero de processos executados.
             tempomedio = exucacaotoatal / (len(processo))

    # Ao final do processo, será aberto um arquivo txt novamente pelo método open utilizanda o metodo " w " ,
    # que permite ao usuario editar o arquivo. Lá será armazenado as informações abaixo.
    arquivo = open('saida.txt', 'w')
    arquivo.write("Tempo total de execução: %d  \n " %(exucacaotoatal))
    arquivo.write("Tempo total de execução processos CPU: %d \n " % (totaldacpu))
    arquivo.write("Tempo total de execução processos ES: %d \n" % (totales))
    arquivo.write("Tempo de espera médio dos processos: %d \n" % (tempomedio))
    arquivo.close()

    # Por fim, fecho a edição do arquivo, abro ele com o método read e mostro o resultado em tela.
    n = open('saida.txt', 'r')
    t = n.read()
    print(t) 
    ´´´
