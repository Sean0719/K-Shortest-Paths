from yen import YenAlgorithm
import sys
import tools
import colorama
import os
import time

def main():
    if len(sys.argv)!=2:
        sys.exit("Programma lanciato con parametri sbagliati: ./my_prog test_file")

    graph, num_nodes, num_arcs, graph_imm_path = tools.getGraphStructure(sys.argv[1])        #Viene creata la struttura dati per il grafo, una MATRICE DELLE ADIACENZE

    colorama.init()

    line = ' '+'*'*31 +'\n'
    line += ' '+'** K SHORTEST LOOPLESS PATHS **'+'\n'
    line += ' '+'**     Algoritmo di Yen      **'+'\n'
    line += ' '+'*'*31
    print(colorama.Fore.YELLOW + line + colorama.Fore.RESET)

    print(colorama.Fore.BLUE + '\n=> E\' stato caricato un grafo con {0} nodi e {1} archi, con una densità d={2:0.1f}'.format(num_nodes, num_arcs, num_arcs/num_nodes) + colorama.Fore.RESET + '\n')

    ans = 'x'
    while ans != 's' and ans != 'n':
        ans = input('Vuoi visualizzare il grafo (s/n)? ')
        ans.lower()

    if ans == 's':
        cmd = 'dot ' + graph_imm_path + '.gv -Tjpeg -o ' + graph_imm_path + '.jpeg'
        os.system(cmd)
        os.popen('eog %U ' + graph_imm_path + '.jpeg')

    print('')
    while True:
        s = int(input('Inserire il nodo sorgente: '))
        t = int(input('Inserire il nodo pozzo: '))
        K = int(input('Inserire il numero di cammini da cercare: '))

        if K == 0:
            sys.exit(colorama.Fore.RED + 'Nessun cammino richiesto...Arrivederci!' + colorama.Fore.RESET)

        if s == t or not 1<=s<=num_nodes or not 1<=t<=num_nodes or K<0:
            print(colorama.Fore.RED + 'ATTENZIONE! Ricontrollare i valore inseriti. Si ricorda che '
                'il nodo sorgente e il nodo pozzo devono essere diversi e K>0 '
                '(K=0 per uscire).'+ colorama.Fore.RESET)
        else:
            break

    start = time.clock()
    shortest_path_tree = YenAlgorithm(graph, s-1, t-1, K)       #Decremento i nodi di uno perché nella struttura dati i nodi partono da 0
    end = time.clock()
    if shortest_path_tree:
        print(colorama.Fore.CYAN)
        tools.printPaths(shortest_path_tree)
        print(colorama.Fore.RESET)

        print(colorama.Fore.GREEN + 'Tempo: {0:.3f}s'.format(end-start) + colorama.Fore.RESET)
    else:
        print(colorama.Fore.RED + 'Nessun cammino tra il nodo sorgente e quello pozzo!' + colorama.Fore.RESET)

if __name__ == '__main__':
    main()