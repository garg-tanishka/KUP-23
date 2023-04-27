from src.extraction.data_extraction import create_graph_individual

if __name__ == "__main__":
    readinput = int(input("Enter a Knolder id: "))
    print(readinput)
    user_id = create_graph_individual(readinput)
