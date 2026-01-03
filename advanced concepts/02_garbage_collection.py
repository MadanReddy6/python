import gc
import ctypes

# We use a custom class to see when it gets destroyed
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
        print(f"Node {self.name} created.")

    def __del__(self):
        print(f"Node {self.name} destroyed/collected.")

    def __repr__(self):
        return f"Node({self.name})"

def demonstrate_garbage_collection():
    print("\n--- Garbage Collection (Cyclic References) ---")
    
    # Ensure GC is enabled
    gc.enable()
    # print(f"GC Debug Flags: {gc.get_debug()}")

    # 1. Create two nodes
    node_a = Node("A")
    node_b = Node("B")

    # 2. Create a cycle
    print("Creating cycle: A -> B and B -> A")
    node_a.next = node_b
    node_b.next = node_a

    # 3. Delete references (Ref count drops, but not to 0 because they point to each other!)
    print("Deleting external references node_a and node_b...")
    del node_a
    del node_b
    
    # At this point, Node A has ref_count=1 (from B), Node B has ref_count=1 (from A).
    # They are unreachable from the root, but ref counting can't delete them.
    # They are "Memory Leaks" if we didn't have a Cyclic GC.
    
    print("External refs deleted. Waiting for GC...")
    
    # 4. Force a collection manually to show it working
    print(f"Objects collected by GC: {gc.collect()}")
    
    print("Done.")

if __name__ == "__main__":
    demonstrate_garbage_collection()
