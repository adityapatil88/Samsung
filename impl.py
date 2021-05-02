import multiprocessing as mp
import os


def create_graph(input_data):
    graph = []
    for row in input_data["relation"]:
        child = row['child']
        parent = row['parent']
        graph.append((parent, child))
    print('relational graph : ', graph)
    return graph


def find_parent(st, gf):
    if type(st) == list:
        res = []
        for i in st:
            res.append([item[0] for item in gf if item[1] == i])
    else:
        res = [item[0] for item in gf if item[1] == st]
    return res


def final(node, graph, output):
    data = []
    temp = find_parent(node, graph)
    for j in temp:
        data.append(find_parent(j, graph))
    data.append(temp)
    res = sum(data, [])
    res.append(node)
    process_info()
    output.put({node: res})


# running process information
def process_info():
    print('Module:' + str(__name__) + '\n')
    print('Parent Process id:' + str(os.getppid()) + '\n')
    print('Process id:' + str(os.getpid()) + '\n\n')


def main(data):
    # Using the queue as the message passing paradigm
    output = mp.Queue()
    graph = create_graph(data)
    processes = [mp.Process(target=final, args=(x, graph, output)) for x in data['node_ids']]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    results = [output.get() for process in processes]

    return results
