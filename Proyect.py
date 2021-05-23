import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
#Nodos del grafo
G.add_node('1', pos = (100,350))
G.add_node('2', pos = (200,350))
G.add_node('3', pos = (300,350))
G.add_node('4', pos = (400,350))
G.add_node('5', pos = (500,350))
G.add_node('6', pos = (600,350))
G.add_node('7', pos = (700,350))
G.add_node('8', pos = (800,350))

G.add_node('9', pos = (814,428))
G.add_node('10', pos = (842,388))
G.add_node('11', pos = (855,332))
G.add_node('12', pos = (842,275))
G.add_node('13', pos = (812,228))
G.add_node('14', pos = (776,198))
G.add_node('15', pos = (710,157))
G.add_node('16', pos = (638,131))
G.add_node('17', pos = (566,116))
G.add_node('18', pos = (490,110))
G.add_node('19', pos = (418,108))
G.add_node('20', pos = (341,114))
G.add_node('21', pos = (287,126))
G.add_node('22', pos = (218,144))
G.add_node('23', pos = (168,175))
G.add_node('24', pos = (119,206))
G.add_node('25', pos = (78,242))
G.add_node('26', pos = (53,289))
G.add_node('27', pos = (43,339))
G.add_node('28', pos = (51,380))
G.add_node('29', pos = (72,419))
G.add_node('30', pos = (123,461))
G.add_node('31', pos = (166,489))
G.add_node('32', pos = (222,515))
G.add_node('33', pos = (287,536))
G.add_node('34', pos = (354,550))
G.add_node('35', pos = (408,558))
G.add_node('36', pos = (489,552))
G.add_node('37', pos = (549,549))
G.add_node('38', pos = (615,537))
G.add_node('39', pos = (663,522))
G.add_node('40', pos = (718,496))
G.add_node('41', pos = (767,466))



#Aristas del grafo
G.add_edge('9', '1', color='red')
G.add_edge('9', '3', color='green')
G.add_edge('9', '5', color='gold')
G.add_edge('9', '6', color='deeppink')
G.add_edge('9', '8', color='limegreen')

G.add_edge('10', '1', color='red')
G.add_edge('10', '2', color='blue')
G.add_edge('10', '4', color='purple')
G.add_edge('10', '8', color='limegreen')

G.add_edge('11', '1', color='red')
G.add_edge('11', '2', color='blue')
G.add_edge('11', '4', color='purple')
G.add_edge('11', '5', color='gold')
G.add_edge('11', '6', color='deeppink')
G.add_edge('11', '7', color='dodgerblue')

G.add_edge('12', '2', color='blue')
G.add_edge('12', '5', color='gold')
G.add_edge('12', '8', color='limegreen')

G.add_edge('13', '5', color='gold')
G.add_edge('13', '3', color='green')
G.add_edge('13', '4', color='purple')

G.add_edge('14', '4', color='purple')
G.add_edge('14', '5', color='gold')
G.add_edge('14', '6', color='deeppink')

G.add_edge('15', '6', color='deeppink')
G.add_edge('15', '7', color='dodgerblue')

G.add_edge('16', '7', color='dodgerblue')
G.add_edge('16', '1', color='red')
G.add_edge('16', '2', color='blue')
G.add_edge('16', '4', color='purple')
G.add_edge('16', '6', color='deeppink')
G.add_edge('16', '3', color='green')
G.add_edge('16', '8', color='limegreen')

G.add_edge('17', '1', color='red')
G.add_edge('17', '2', color='blue')
G.add_edge('17', '4', color='purple')
G.add_edge('17', '5', color='gold')
G.add_edge('17', '6', color='deeppink')
G.add_edge('17', '7', color='dodgerblue')
G.add_edge('17', '8', color='limegreen')

G.add_edge('18', '4', color='purple')
G.add_edge('18', '8', color='limegreen')
G.add_edge('18', '1', color='red')
G.add_edge('18', '6', color='deeppink')
G.add_edge('18', '7', color='dodgerblue')
G.add_edge('18', '2', color='blue')
G.add_edge('18', '5', color='gold')

G.add_edge('19', '8', color='limegreen')
G.add_edge('19', '7', color='dodgerblue')
G.add_edge('19', '6', color='deeppink')
G.add_edge('19', '1', color='red')
G.add_edge('19', '4', color='purple')

G.add_edge('20', '1', color='red')
G.add_edge('20', '3', color='green')
G.add_edge('20', '4', color='purple')
G.add_edge('20', '5', color='gold')
G.add_edge('20', '7', color='dodgerblue')
G.add_edge('20', '2', color='blue')
G.add_edge('20', '8', color='limegreen')

G.add_edge('21', '1', color='red')
G.add_edge('21', '6', color='deeppink')
G.add_edge('21', '7', color='dodgerblue')
G.add_edge('21', '8', color='limegreen')
G.add_edge('21', '4', color='purple')

G.add_edge('22', '1', color='red')
G.add_edge('22', '7', color='dodgerblue')

G.add_edge('23', '1', color='red')
G.add_edge('23', '2', color='blue')
G.add_edge('23', '8', color='limegreen')
G.add_edge('23', '4', color='purple')
G.add_edge('23', '6', color='deeppink')
G.add_edge('23', '7', color='dodgerblue')

G.add_edge('24', '1', color='red')
G.add_edge('24', '2', color='blue')
G.add_edge('24', '3', color='green')
G.add_edge('24', '8', color='limegreen')

G.add_edge('25', '2', color='blue')
G.add_edge('25', '4', color='purple')
G.add_edge('25', '5', color='gold')

G.add_edge('26', '3', color='green')
G.add_edge('26', '5', color='gold')

G.add_edge('27', '4', color='purple')
G.add_edge('27', '2', color='blue')

G.add_edge('28', '3', color='green')
G.add_edge('28', '4', color='purple')
G.add_edge('28', '5', color='gold')

G.add_edge('29', '3', color='green')
G.add_edge('29', '1', color='red')
G.add_edge('29', '8', color='limegreen')

G.add_edge('30', '1', color='red')
G.add_edge('30', '2', color='blue')
G.add_edge('30', '6', color='deeppink')
G.add_edge('30', '7', color='dodgerblue')
G.add_edge('30', '8', color='limegreen')

G.add_edge('31', '3', color='green')
G.add_edge('31', '5', color='gold')
G.add_edge('31', '6', color='deeppink')
G.add_edge('31', '1', color='red')
G.add_edge('31', '4', color='purple')
G.add_edge('31', '8', color='limegreen')

G.add_edge('32', '4', color='purple')
G.add_edge('32', '2', color='blue')

G.add_edge('33', '4', color='purple')
G.add_edge('33', '2', color='blue')

G.add_edge('34', '8', color='limegreen')
G.add_edge('34', '2', color='blue')
G.add_edge('34', '1', color='red')
G.add_edge('34', '6', color='deeppink')

G.add_edge('35', '6', color='deeppink')
G.add_edge('35', '7', color='dodgerblue')
G.add_edge('35', '8', color='limegreen')
G.add_edge('35', '4', color='purple')
G.add_edge('35', '1', color='red')

G.add_edge('36', '4', color='purple')
G.add_edge('36', '2', color='blue')

G.add_edge('37', '5', color='gold')
G.add_edge('37', '6', color='deeppink')
G.add_edge('37', '8', color='limegreen')
G.add_edge('37', '1', color='red')
G.add_edge('37', '3', color='green')
G.add_edge('37', '2', color='blue')

G.add_edge('38', '4', color='purple')
G.add_edge('38', '5', color='gold')

G.add_edge('39', '4', color='purple')
G.add_edge('39', '2', color='blue')

G.add_edge('40', '4', color='purple')
G.add_edge('40', '5', color='gold')

G.add_edge('41', '1', color='red')
G.add_edge('41', '5', color='gold')
G.add_edge('41', '3', color='green')
G.add_edge('41', '8', color='limegreen')
G.add_edge('41', '4', color='purple')
G.add_edge('41', '6', color='deeppink')
G.add_edge('41', '2', color='blue')





# VARIABLES GLOBALES
Tacticas = ['1', '2', '3', '4', '5', '6', '7', '8']

C1 = ['13', '14', '18', '22', '28', '33', '36', '37']
C2 = ['10', '20', '29', '30', '32', '34', '38', '39']
C3 = ['12', '15', '16', '19', '24', '27', '41']
C4 = ['9', '11', '17', '21', '23', '25', '26', '31', '35', '40']



Attacks_names = {'1':'Initial Access', '2':'Execution', '3':'Privilege Escaletion',
        '4':'Defense Evasion', '5':'Credential Access', '6':'Exfiltration',
        '7':'Command and Control', '8':'Impact'}
Tecnicas_names = {'9':'Admin Access', '10':'API Monitoring', '11':'Application Diversity',
                  '12':'Backup and Recovery', '13':'Baselina', '14':'Behavioral Analytics',
                  '15':'Burn-In', '16':'Decoy Account', '17':'Decoy Content',
                  '18':'Decoy Credentials', '19':'Decoy Diversity', '20':'Decoy Network',
                  '21':'Decoy Persona', '22':'Decoy Process', '23': 'Decoy System',
                  '24':'Detonate Malware', '25':'Email Manipulation',
                  '26':'Hardware Manipulation', '27':'Hunting', '28':'Isolation',
                  '29':'Migrate Attack Vector', '30':'Network Diversity',
                  '31':'Network Manipulation', '32': 'Network Monitoring',
                  '33':'PCAP Collection', '34':'Peropheral Management',
                  '35':'Pocket Litter', '36':'Protocol Decoder', '37':'Security Controls',
                  '38':'Standard Operating Procedure', '39':'System Activity Monitoring',
                  '40':'User Training', '41':'Software Manipulation'}

L1 = ['16', '18', '15', '39', '37', '29', '28', '23', '20', '19', '25', '40', '21'] # Initial Access
L2 = ['9', '37', '23', '39', '41', '10', '11', '24', '38'] # Execution
L3 = ['13', '9', '23', '39', '37', '16', '18', '15', '41', '14'] # Privilege Escaletion
L4 = ['41', '9', '37', '23', '14', '16', '18', '15', '13', '39', '10', '32', '11',
     '24', '35', '17', '38', '19'] # Defense Evasion
L5 = ['18', '41', '22', '30', '17', '39', '37', '38', '31', '11', '40', '15', '32'] # Credential Access
L6 = ['37', '33', '36', '32', '31', '34', '14'] # Exfiltration
L7 = ['33', '36', '31', '32', '34', '29', '14', '28', '23', '27'] # Command and Control
L8 = ['12', '41', '39', '14', '31', '37', '23', '17'] # Impact


Attacks = {'1':L1, '2':L2, '3':L3, '4':L4, '5':L5, '6':L6, '7':L7, '8':L8}
for q in Attacks_names:
    print(q, "->", Attacks_names[q])


# FUNCIONES
def create_copy(graph):
    new_G = graph.copy()
    return new_G

def create_attack_graph(graph, attack):
    new_G = graph.copy()
    for node in graph.nodes():
        if node not in Tacticas:
            if node not in Attacks[str(attack)]:
                new_G.remove_node(node)
    return new_G


def first_attack(graph,attack):
    new_G = create_attack_graph(graph,attack)
    return new_G

def interseccion(A,B):
    lista_final = []
    for i in A:
        if (i not in lista_final) and (i in B):
            lista_final.append(i)
    return lista_final

def path_without_edge(graph, path):
    h = []
    if len(path) >= 4:
        for i in range(len(path)):
            if i <= len(path)-2:
                j = (path[i], path[i+1])
                h.append(j)
        h.pop(0)
        h.pop(-1)
        u, v = h[len(h)//2]
        # print('u: ', u, 'v: ', v)
        graph.remove_edge(u, v)
    elif len(path) == 2:
        j = (path[0], path[1])
        h.append(j)
        u, v = h[0]
        # print('u: ', u, 'v: ', v)
        graph.remove_edge(u, v)
    elif len(path) == 3:
        j = (path[0], path[1])
        h.append(j)
        k = (path[1], path[2])
        h.append(k)
        u, v = h[len(h)//2]
        # print('u: ', u, 'v: ', v)
        graph.remove_edge(u, v)
    return graph


def dijkstra_with_backtracking(graph,newC):
    copy_graph = graph.copy()
    path = []
    new_C1 = newC[0]
    new_C2 = newC[1]
    new_C3 = newC[2]
    new_C4 = newC[3]
    if len(new_C1)==0:
        return path
    if len(new_C2)==0:
        return path
    if len(new_C3)==0:
        return path
    if len(new_C4)==0:
        return path
    path.append(new_C1[0])
    for q in range(0,3):
        n1 = list(copy_graph.neighbors(path[-1]))
        if len(n1) == 0:
            return path
        path.append(n1[0])
        count = 0
        while True:
            n = list(copy_graph.neighbors(n1[count]))
            for i in n:
                if i in newC[q+1]:
                    path.append(i)
                    break
            if path[-1] in newC[q+1]:
                break
            else:
                path.pop(-1)
                count += 1
                if len(n1) <= count:
                    break
                path.append(n1[count])
        if path[-1] in newC[q]:
            empty_list = []
            return empty_list
    return path

def all_paths(graph):
    L = []
    copy_graph = create_copy(graph)
    new_C1 = interseccion(C1,copy_graph.nodes())
    new_C2 = interseccion(C2,copy_graph.nodes())
    new_C3 = interseccion(C3,copy_graph.nodes())
    new_C4 = interseccion(C4,copy_graph.nodes())
    newC = []
    newC.append(new_C1)
    newC.append(new_C2)
    newC.append(new_C3)
    newC.append(new_C4)
    while True:
        path = dijkstra_with_backtracking(copy_graph,newC)
        if len(path) == 0:
            break
        L.append(path)
        aux_graph = path_without_edge(copy_graph, path)
        copy_graph = aux_graph
    for i in newC:
        if len(i) > 1:
            size_Ci = len(i)
            for q in range(1,size_Ci):
                copy_graph = create_copy(graph)
                i.pop(0)
                while True:
                    path = dijkstra_with_backtracking(copy_graph,newC)
                    if len(path) == 0:
                        break
                    L.append(path)
                    aux_graph = path_without_edge(copy_graph, path)
                    copy_graph = aux_graph
    return L

def final_list(graph):
    L = all_paths(graph)

    for q in L:
        for i in range(4):
            if q[i] in Tacticas:
                q.pop(i)
    Li = []
    for j in L:
        if j not in Li:
            Li.append(j)
    return Li

def convert_edges(paths):
    h = []
    for q in paths:
        for i in range(len(q)):
            if i <= len(q)-2:
                j = (q[i], q[i+1])
                k = (q[i+1], q[i])
                h.append(j)
                h.append(k)
    return h

def final_nodes(paths):
    h = []
    for q in paths:
        for i in q:
            h.append(i)
    n = list(set(h))
    return n


# MAIN
A = input()

# Copiamos el grafo original
copy_G = create_copy(G)
new_G = create_attack_graph(copy_G,A)
copy_new = create_copy(new_G)

# Creamos los caminos
path = all_paths(copy_new)
final_path = final_list(copy_new)
# for q in path:
#     print(q)
# for q in final_path:
#     print(q)
Names_list = []
for q in final_path:
    for index, value in enumerate(q):
        q[index] = Tecnicas_names[value]
    print(q)

        # for j in range(1,5):
        # Names_list.append(Tecnicas_names[q])
        # print(Names_list)
        # Names_list = []

# Miramos aristas y nodos de los caminos
aristas = convert_edges(path)
comparacion = []
for item in new_G.edges():
  if item not in aristas:
    comparacion.append(item)
new_G.remove_edges_from(comparacion)

nodos = final_nodes(path)
for node in copy_new:
    if node not in nodos:
        new_G.remove_node(node)




# DIBUJA EL GRAFO

color_map = []
for node in new_G:
    if node == '1':
        color_map.append('red')
    elif node == '2':
        color_map.append('blue')
    elif node == '3':
        color_map.append('green')
    elif node == '4':
        color_map.append('purple')
    elif node == '5':
        color_map.append('gold')
    elif node == '6':
        color_map.append('deeppink')
    elif node == '7':
        color_map.append('dodgerblue')
    elif node == '8':
        color_map.append('limegreen')
    else:
        color_map.append('black')


size_map = []
for node in new_G:
    if node in Tacticas:
        size_map.append(200)
    else:
        size_map.append(100)



pos = nx.get_node_attributes(new_G, 'pos')
colors = nx.get_edge_attributes(new_G,'color').values()


nx.draw(new_G, pos, edge_color = colors, with_labels = True, node_size = size_map, font_size = 6,
        node_color = color_map, font_color = 'white')


plt.show()
