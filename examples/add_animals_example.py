from Aqua import Aqua

def run_example():
    myaqua = Aqua(50, 30)
    myaqua.add_animal("scalarfish1", 4, 10, 10, 1, 0, 'sc')
    myaqua.add_animal("molyfish2", 12, 35, 15, 0, 1, 'mo')
    myaqua.print_board()

if __name__ == "__main__":
    run_example()