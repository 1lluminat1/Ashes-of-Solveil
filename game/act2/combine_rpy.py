import os

# Get the current directory where the script is running
current_dir = os.getcwd()

# Output file name
output_file = "combined_scripts.txt"

# List all .rpy files in the current directory
rpy_files = [f for f in os.listdir(current_dir) if f.endswith('.rpy')]

# Sort them alphabetically for consistent order
rpy_files.sort()

# Open the output file in write mode
with open(output_file, 'w', encoding='utf-8') as outfile:
    for rpy_file in rpy_files:
        # Write a header for each file to separate them clearly
        outfile.write(f"=== Contents of {rpy_file} ===\n\n")
        
        # Read the content of the .rpy file and append it
        with open(rpy_file, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
        
        # Add some spacing after each file
        outfile.write("\n\n=== End of {rpy_file} ===\n\n")

print(f"Combined {len(rpy_files)} .rpy files into {output_file}.")