class graph:
    class Undirected:
        class Vertex:
            def __init__(self, key):
                self.key = key
                self.neighbors = set()

        @staticmethod
        def add_vertex(graph, key):
            if key not in graph.vertices:
                graph.vertices[key] = graph.Undirected.Vertex(key)

        @staticmethod
        def add_edge(graph, key1, key2):
            if key1 in graph.vertices and key2 in graph.vertices:
                graph.vertices[key1].neighbors.add(key2)
                graph.vertices[key2].neighbors.add(key1)

        @staticmethod
        def remove_vertex(graph, key):
            if key in graph.vertices:
                del graph.vertices[key]
                for vertex in graph.vertices.values():
                    if key in vertex.neighbors:
                        vertex.neighbors.remove(key)

        @staticmethod
        def remove_edge(graph, key1, key2):
            if key1 in graph.vertices and key2 in graph.vertices:
                if key2 in graph.vertices[key1].neighbors:
                    graph.vertices[key1].neighbors.remove(key2)
                if key1 in graph.vertices[key2].neighbors:
                    graph.vertices[key2].neighbors.remove(key1)

        @staticmethod
        def print_graph(graph):
            print("Undirected Graph Vertices:")
            print([vertex.key for vertex in graph.vertices.values()])
            print("Undirected Graph Edges:")
            for key, vertex in graph.vertices.items():
                print(f"{vertex.key}: {list(vertex.neighbors)}")

    class Directed:
        class Vertex:
            def __init__(self, key):
                self.key = key
                self.out_neighbors = set()
                self.in_neighbors = set()

        @staticmethod
        def add_vertex(graph, key):
            if key not in graph.vertices:
                graph.vertices[key] = graph.Directed.Vertex(key)

        @staticmethod
        def add_edge(graph, from_key, to_key):
            if from_key in graph.vertices and to_key in graph.vertices:
                graph.vertices[from_key].out_neighbors.add(to_key)
                graph.vertices[to_key].in_neighbors.add(from_key)

        @staticmethod
        def remove_vertex(graph, key):
            if key in graph.vertices:
                del graph.vertices[key]
                for vertex in graph.vertices.values():
                    if key in vertex.out_neighbors:
                        vertex.out_neighbors.remove(key)
                    if key in vertex.in_neighbors:
                        vertex.in_neighbors.remove(key)

        @staticmethod
        def remove_edge(graph, from_key, to_key):
            if from_key in graph.vertices and to_key in graph.vertices:
                if to_key in graph.vertices[from_key].out_neighbors:
                    graph.vertices[from_key].out_neighbors.remove(to_key)
                if from_key in graph.vertices[to_key].in_neighbors:
                    graph.vertices[to_key].in_neighbors.remove(from_key)

        @staticmethod
        def print_graph(graph):
            print("\nDirected Graph Vertices:")
            print([vertex.key for vertex in graph.vertices.values()])
            print("Directed Graph Outgoing Edges:")
            for key, vertex in graph.vertices.items():
                print(f"{vertex.key} -> {list(vertex.out_neighbors)}")
            print("Directed Graph Incoming Edges:")
            for key, vertex in graph.vertices.items():
                print(f"{vertex.key} <- {list(vertex.in_neighbors)}")

    #  END OF GRAPH  #