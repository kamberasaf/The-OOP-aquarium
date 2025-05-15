from aqua import Aqua

def run_example():
    myaqua = Aqua(50, 30)
    
    success1 = myaqua.add_animal("scalarfish1", 4, 10, 10, 1, 0, 'sc')
    print(f"Adding scalarfish1 successful? {success1}")
    
    success2 = myaqua.add_animal("molyfish2", 12, 35, 15, 0, 1, 'mo')
    print(f"Adding molyfish2 successful? {success2}")
    
    print("\nAquarium board:")
    myaqua.print_board()

if __name__ == "__main__":
    run_example()
