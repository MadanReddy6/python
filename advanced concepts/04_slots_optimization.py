import sys
import timeit

class Pixel:
    """Standard Class"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class PixelSlots:
    """Optimized Class with __slots__"""
    __slots__ = ['x', 'y', 'z']
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def demonstrate_slots():
    print("\n--- __slots__ Optimization ---")
    print("Explanation: Standard classes use a dictionary (__dict__) to store attributes, allowing dynamic addition.")
    print("__slots__ tells Python: 'These are the only attributes I will ever have', removing the need for internal __dict__.\n")

    # 1. Memory Usage Comparison
    p1 = Pixel(10, 20, 30)
    p2 = PixelSlots(10, 20, 30)

    # We use sys.getsizeof to check shallow size
    # Note: getsizeof doesn't recursively measure referenced objects, but it gives us the object overhead.
    
    # A standard object has a __dict__ and often a __weakref__
    size_std = sys.getsizeof(p1) + sys.getsizeof(p1.__dict__) 
    size_slots = sys.getsizeof(p2) # No __dict__
    
    print(f"Size of single Standard Pixel (approx overhead): {size_std} bytes")
    print(f"Size of single Slotted Pixel (approx overhead):  {size_slots} bytes")
    
    savings = (1 - size_slots/size_std) * 100
    print(f"Memory Savings: ~{savings:.1f}% per instance!")

    # 2. Performance Comparison (Attribute Access)
    print("\nRunning performance test (accessing attributes 10 million times)...")
    
    t1 = timeit.timeit('p1.x', globals=locals(), number=10_000_000)
    t2 = timeit.timeit('p2.x', globals=locals(), number=10_000_000)
    
    print(f"Standard Access Time: {t1:.4f} sec")
    print(f"Slots Access Time:    {t2:.4f} sec")
    
    if t2 < t1:
        print("Result: __slots__ is faster!")
    else:
        print("Result: Diff is negligible for simple cases (or machine dependent noise).")

if __name__ == "__main__":
    demonstrate_slots()
