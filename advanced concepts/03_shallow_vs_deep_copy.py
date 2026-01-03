import copy

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members  # This is a list (mutable object)

    def __repr__(self):
        return f"Team(name='{self.name}', members={self.members})"

def demonstrate_copying():
    print("\n--- Shallow vs Deep Copy ---")
    
    # Setup
    original_team = Team("Alpha", ["Alice", "Bob"])
    print(f"Original: {original_team}")

    # 1. Assignment (Not a copy!)
    # Both variables point to the exact same object in memory.
    assigned_team = original_team
    
    # 2. Shallow Copy
    # Creates a NEW Team object, but inserts references to the original inner objects (the list).
    shallow_team = copy.copy(original_team)
    shallow_team.name = "Beta" # Changing primitive/string is fine (strings are immutable, references change)
    
    # 3. Deep Copy
    # Creates a NEW Team object AND recursively copies all inner objects.
    deep_team = copy.deepcopy(original_team)
    deep_team.name = "Gamma"
    
    print("\n[Action] Adding 'Charlie' to the original team's members list...")
    original_team.members.append("Charlie")
    
    # Results
    print(f"\n1. Original Team: {original_team}")
    print(f"   (Alice, Bob, Charlie) -> Expected")
    
    print(f"\n2. Assigned Team (variable assignment): {assigned_team}")
    print(f"   (Alice, Bob, Charlie) -> Expected (Same object)")
    
    print(f"\n3. Shallow Copy Team (copy.copy): {shallow_team}")
    print(f"   (Alice, Bob, Charlie) -> !!! SURPRISE !!!")
    print("   Analysis: The 'Team' object was new, but the 'members' list was shared!")
    
    print(f"\n4. Deep Copy Team (copy.deepcopy): {deep_team}")
    print(f"   (Alice, Bob) -> Expected (Completely independent)")

if __name__ == "__main__":
    demonstrate_copying()
