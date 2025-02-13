import json
import re
import os

# Main script
def process_local_file(file_path):
    # Read local file
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except Exception as e:
        raise Exception(f"Error while reading a file: {e}")

    # Make a output folder
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    # Block types 
    grouped_blocks = {}

    # Block search
    pattern = re.compile(r"block\.([a-zA-Z0-9_]+)\.([a-zA-Z0-9_]+)")

    # Search for keys in JSON
    for key in data:
        match = pattern.match(key)
        if match:
            mod_name = match.group(1)  # Mod name
            block_name = match.group(2)  # Block name

            # Tranform to (Mod name):(Block name)
            formatted_block = f"{mod_name}:{block_name}"

            # Group block by types (grass, metal, glass)
            block_type = block_name.split("_")[0]  # First part of block name
            if block_type not in grouped_blocks:
                grouped_blocks[block_type] = []
            grouped_blocks[block_type].append(formatted_block)

    # Write results in file
    for block_type, blocks in grouped_blocks.items():
        output_file = os.path.join(output_folder, f"{block_type}.txt")
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(" ".join(blocks))

    print(f"Results are writed in folder {output_folder}.")

if __name__ == "__main__":
    file_path = input("Enter a path to en_us.json on your pc: ")
    try:
        process_local_file(file_path)
    except Exception as e:
        print(f"Error: {e}")
