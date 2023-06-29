"""
Script to compare two files and return a matching score for each row id that exist
It will apply a regular expression to match the format "4, 22" and ignore anything else
"""

import re

def compare_files(file1, file2):
    pattern = re.compile(r'(\d+),\s+(\d+)')  # regular expression to match "4, 22" format
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()

    total_lines = len(f1_lines)
    matched_lines = 0

    for i in range(total_lines):
        match1 = re.search(pattern, f1_lines[i])
        if match1:
            file1_id, file1_value = match1.groups()
            match2 = re.search(f'{file1_id},\\s+(\\d+)', ''.join(f2_lines))
            if match2:
                file2_value = match2.group(1)
                if file1_value == file2_value:
                    matched_lines += 1
                else:
                    print(f"Not matching: File 1: {file1_id}, {file1_value} <#> File 2: {file1_id}, {file2_value}")
            else:
                print(f"Not found: File 1: {file1_id}, {file1_value}")

    matching_score = (matched_lines / total_lines) * 100
    print(f"\nMatching score: {matching_score:.2f}%\n")

if __name__ == "__main__":
    print("\nRunning Compare Reviews Script...\n")
    compare_files('./reviews_dir/output_compare.txt', './reviews_dir/manual_reviews_mapped.txt')