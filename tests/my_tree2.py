import os

def filter_directory_structure(root_dir, excluded_dirs):
    structure = []
    included_dirs = set()  # Set to track included directories

    def add_structure(current_dir, level, is_last, is_first):
        # Check if the current directory is excluded
        if os.path.basename(current_dir) in excluded_dirs:
            return  # Skip this directory

        # Prepare the indentation for the current level
        
        # indent = ' ' * 4 * level
        #Pero no es lo mismo para las carpetas que para los ficheros.. de primer nivel
        indent = ' ' * 4 * (level - 1) if is_first else ' ' * 4 * level

        vertical = '│   ' * level  # Vertical bars for the current level
        dir_name = os.path.basename(current_dir)

        # Add the current directory to the structure if not included before and not the first
        if not is_first:
            structure.append(f"{vertical}{indent}{dir_name}/")
            included_dirs.add(current_dir)  # Mark this directory as included

        # Get the entries in the current directory
        entries = sorted(os.listdir(current_dir))

        # Separate files and subdirectories
        subdirs = [entry for entry in entries if os.path.isdir(os.path.join(current_dir, entry))]
        files = [entry for entry in entries if os.path.isfile(os.path.join(current_dir, entry))]

        # Process each file
        for j, file in enumerate(files):

            if j == len(files) - 1:  # Last file
                structure.append(f"├── {file}") if (level == 0) else structure.append(f"{vertical}{indent}    └── {file}")
                # structure.append(f"{vertical}{indent}    └── {file}")
            else:
                # structure.append(f"{vertical}{indent}    ├── {file}")
                structure.append(f"├── {file}") if (level == 0) else structure.append(f"{vertical}{indent}    ├── {file}")

        # Process each subdirectory recursively
        for i, entry in enumerate(subdirs):
            subdir_path = os.path.join(current_dir, entry)
            is_last_subdir = (i == len(subdirs) - 1)  # Check if this is the last subdirectory
            connector = '└── ' if is_last_subdir else '├── '
            structure.append(f"{vertical}{indent}{connector}{entry}/")
            # Recursive call for subdirectory, next level, and not first
            # add_structure(subdir_path, level + 1, is_last_subdir, False)
            add_structure(subdir_path, level + 1, is_last_subdir, True) # Si que es el primero cada vez


    # Start adding structure from the root directory
    # add_structure(root_dir, 0, False, True)  # Pass True for the first call
    add_structure(root_dir, 0, False, False)  

    return structure

if __name__ == "__main__":
    # Define the root directory as the parent of the app directory
    root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Parent of 'app'
    
    # Directories to exclude
    excluded_directories = ['envCV', "__pycache__", ".git", "tests",]  # Directories to ignore   

    # Get the filtered directory structure
    filtered_structure = filter_directory_structure(root_directory, excluded_directories)
    
    # Write the output to a text file in the tests folder
    output_file = os.path.join(os.path.dirname(__file__), 'directory_structure.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in filtered_structure:
            f.write(line + '\n')

    print(f"Directory structure has been written to {output_file}.")
