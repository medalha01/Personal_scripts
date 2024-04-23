import csv

def parse_data_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  # Ensure correct encoding is used
        lines = [line.strip() for line in file if line.strip()]  # Read lines, ignoring empty ones
    
    # Initialize variables
    data = []
    num_lines_per_record = 4
    total_lines = len(lines)
    
 


    # Process each block of lines
    i = 0
    
    while i < total_lines:
        list_of_values = []
        if i + num_lines_per_record <= total_lines:
            for j in range(0, 4):
                value = lines[i + j]
                if value == "Release":
                    i += 3
                    value = lines[i+j]
                list_of_values.append(value)
            

                    
            data.append(list_of_values)
            i += num_lines_per_record
        else:
            print(f"Not enough data to form a record at line {i}. Expected {num_lines_per_record} lines, found {total_lines - i}.")
            break

    return data

def write_to_csv(data, output_file_path):
    headers = ['Game', 'Year', 'Rating', 'Price']
    with open(output_file_path, 'w', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

# Example usage
input_file_path = 'Best Games Steam.txt'  # Path to the input .txt file
output_file_path = 'output.csv'  # Path to the output .csv file

game_data = parse_data_from_txt(input_file_path)
if game_data:  # Only write to CSV if data was parsed successfully
    write_to_csv(game_data, output_file_path)
else:
    print("No data was parsed successfully. Check the input file format.")
