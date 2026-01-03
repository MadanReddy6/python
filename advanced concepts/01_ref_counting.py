import sys
import ctypes

def ref_count_address(address):
    """Helper to get ref count using memory address, 
    so we don't accidentally increase it by passing the object itself."""
    return ctypes.c_long.from_address(address).value

def demonstrate_ref_counting():
    print("--- Reference Counting Demonstration ---")
    
    # 1. Create an object (a list)
    # The literal [1, 2, 3] is created on the Heap.
    # 'my_list' is a reference on the Stack pointing to it.
    my_list = [1, 2, 3] 
    
    # Get memory address
    addr = id(my_list)
    
    print(f"1. Created my_list. Ref count: {sys.getrefcount(my_list)}")
    # Note: sys.getrefcount() returns 2 because the argument passed to it
    # creates a temporary reference usually.
    
    # 2. Create another reference
    alias_list = my_list
    print(f"2. Created alias_list. Ref count: {sys.getrefcount(my_list)}")
    
    # 3. Delete one reference
    del alias_list
    print(f"3. Deleted alias_list. Ref count: {sys.getrefcount(my_list)}")
    
    # 4. Delete the original reference
    # We can't use sys.getrefcount(my_list) because my_list is gone.
    # We check the memory address directly using ctypes (dangerous but educational).
    del my_list
    
    # Ideally, the memory is now freed or marked for reuse.
    # The count at that address might be garbage now or 0 if we could check safely immediately.
    print("4. Deleted my_list. The object [1, 2, 3] is now eligible for immediate reclamation.")
    print("   (We cannot safely check ref count of a deleted object without risk of crashing or reading garbage)")

if __name__ == "__main__":
    demonstrate_ref_counting()
