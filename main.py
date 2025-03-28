def filter_lines(filename, keyword):
    with open(filename, 'r') as infile:
        lines = infile.readlines()
    filtered_lines = [line for line in lines if keyword in line]
    with open('filtered.txt', 'w') as outfile:
        outfile.writelines(filtered_lines)


filter_lines('text.txt', 'incididunt')
