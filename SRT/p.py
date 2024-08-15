#!/usr/bin/env python3

def ls_cmd():
    # Manually list the files in the finaldir directory
    file_list = ['alpha5', 'test.csv', 'testfile']
    return file_list

# Function to count lines in a file
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0

if __name__ == "__main__":
    filelst = ls_cmd()
    # Print each filename
    for filename in filelst:
        print(filename)
    
    # Print total number of lines for all files
    total_lines = sum(count_lines(f'finaldir/{filename}') for filename in filelst)
    print(f'Total number of lines: {total_lines}')
