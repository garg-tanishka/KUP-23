from src.data_analysis.leader_board_analysis import create_graph_individual

if __name__ == "__main__":
    readinput = int(input("Enter a Knolder id: "))
    print(readinput)
    user_id = create_graph_individual(readinput)
