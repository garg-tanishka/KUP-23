from src.knolder_employee_score_extraction.data_extraction import Plot_Class

if __name__ == "__main__":
    read_input = int(input("Enter Your Knolder ID: "))
    print(read_input)
    user_id = Plot_Class(read_input)
