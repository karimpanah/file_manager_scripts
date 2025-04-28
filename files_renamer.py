# Batch file renamer - Renames files in target folder based on source folder filenames (keeping target extensions)

import os
from pathlib import Path

def rename_files(source_folder, target_folder):
    """
    Renames files in target folder using names from source folder files (preserves target file extensions)
    
    Parameters:
    - source_folder: Folder containing source files for new names
    - target_folder: Folder containing target files to be renamed
    """
    try:
        source_path = Path(source_folder)
        target_path = Path(target_folder)
        
        if not source_path.exists() or not source_path.is_dir():
            raise FileNotFoundError(f"Source folder not found: {source_folder}")
            
        if not target_path.exists() or not target_path.is_dir():
            raise FileNotFoundError(f"Target folder not found: {target_folder}")
        
        source_files = sorted([f.name for f in source_path.glob('*') if f.is_file()])
        target_files = sorted([f.name for f in target_path.glob('*') if f.is_file()])
        
        if not source_files or not target_files:
            print("Warning: One of the folders is empty")
            return
            
        num_files = min(len(source_files), len(target_files))
        renamed_count = 0
        
        for i in range(num_files):
            source_name = source_files[i]
            old_target_name = target_files[i]
            
            source_stem = Path(source_name).stem
            target_extension = Path(old_target_name).suffix
            
            new_target_name = f"{source_stem}{target_extension}"
            
            old_path = target_path / old_target_name
            new_path = target_path / new_target_name
            
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_target_name} -> {new_target_name}")
                renamed_count += 1
            except Exception as e:
                print(f"Error renaming {old_target_name}: {str(e)}")
        
        print(f"\nTotal files renamed: {renamed_count}/{num_files}")
        
    except Exception as e:
        print(f"System error: {str(e)}")

# Example usage:
if __name__ == "__main__":
    source = "path/to/source_folder"
    target = "path/to/target_folder"
    
    rename_files(source, target)