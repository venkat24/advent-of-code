from copy import copy

class Node:
    def __init__(self, name, depth, parent):
      self.name = name
      self.depth = depth
      self.parent = parent

    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"{{ {self.name} : {self.depth}  }}"

if __name__ == "__main__":
    with open ("input.txt", "r") as f:
        edges = []
        nodelist = {}
        for line in f:
            edges.append(tuple(line.strip().split(")")))

        COM = edges[0][0]

        for edge in edges:
            parent_name = edge[0]
            child_name = edge[1]

            parent = None
            child = None

            if parent_name in nodelist.keys():
                parent = nodelist[parent_name]
            else:
                parent = Node(parent_name, 0, None)

            if child_name in nodelist.keys():
                child = nodelist[child_name]
            else:
                child = Node(child_name, 0, None)

            child.parent = parent
            child.depth = parent.depth + 1

            nodelist[parent_name] = parent
            nodelist[child_name] = child

        sum = 0
        for name, node in nodelist.items():
            current = node

            count = 0
            while current != None and current.name != COM:
                # print(current.name + " -> ", end='')
                count += 1
                current = current.parent

            sum += count

        print(sum)
