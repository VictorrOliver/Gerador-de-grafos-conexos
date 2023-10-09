import networkx as nx
import random
import matplotlib.pyplot as plt

def criar_grafo(vertices, arestas):
    if arestas < vertices - 1:
        print("O número mínimo de arestas para um grafo conectado é", vertices - 1)
        return None, None

    max_arestas = (vertices * (vertices - 1)) / 2
    if arestas > max_arestas:
        print(f"Erro: O número máximo de arestas para {vertices} vértices é {int(max_arestas)}.")
        return None, None

    G = nx.Graph()

    # Adicionar vértices ao grafo
    G.add_nodes_from(range(vertices))

    # Cria uma árvore geradora mínima
    for i in range(1, vertices):
        u = i
        v = random.randint(0, i - 1)
        G.add_edge(u, v)

    # Converter os nós em uma lista para uso com random.sample()
    nodes_list = list(G.nodes())

    # Adicionar arestas adicionais aleatórias até atingir o número desejado de arestas
    while G.number_of_edges() < arestas:
        u, v = random.sample(nodes_list, 2)
        if not G.has_edge(u, v):
            G.add_edge(u, v)

    # Gerar a lista de adjacência
    lista_adjacencia = {}
    for node in G.nodes():
        lista_adjacencia[node] = list(G.neighbors(node))

    return G, lista_adjacencia

def escrever_lista_adjacencia(arquivo, lista_adjacencia):
    with open(arquivo, 'w') as f:
        f.write(f"{len(lista_adjacencia)}\n")
        for node, neighbors in lista_adjacencia.items():
            neighbors_str = " ".join(map(str, neighbors))
            f.write(f"{node}    {neighbors_str}\n")

while True:
    print("Opções:")
    print("1. Gerar um novo grafo ")
    print("2. Sair")

    opcao = input("Escolha uma opção: ")
    print()

    if opcao == '1':
        # Quantidade desejada de vértices e arestas
        num_vertices = int(input("Digite a quantidade desejada de vértices: "))
        num_arestas = int(input("Digite a quantidade desejada de arestas: "))
        print()

        grafo, lista_adjacencia = criar_grafo(num_vertices, num_arestas)
        if grafo:
            nome_arquivo = input("Nome do arquivo: ")
            escrever_lista_adjacencia(nome_arquivo, lista_adjacencia)
            print("Grafo criado com sucesso.")
            nx.draw(grafo, with_labels=True)
            plt.show()
                
    elif opcao == '2':
        break

    else:
        print("Opção inválida. Escolha 1, ou 2.")
