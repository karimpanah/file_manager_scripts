# 🔀 Batch File Renamer

A simple yet powerful Python script to rename files in a target folder based on the filenames in a source folder, while intelligently preserving the original file extensions of the target files.

---

### 🤔 The Problem it Solves

Imagine you have two folders with related, but inconsistently named, files:

* **`Source Folder`** (contains the correct names):
    * `Project_Report_Final.txt`
    * `Data_Analysis.xlsx`
    * `Presentation_Slides.pptx`

* **`Target Folder`** (contains the files you want to rename):
    * `DOC001.pdf`
    * `sheet_v2.csv`
    * `slides_draft.key`

You want the files in the `Target Folder` to match the names from the `Source Folder` but **keep their own extensions** (e.g., you want `DOC001.pdf` to become `Project_Report_Final.pdf`). Renaming hundreds of files like this manually is tedious and prone to errors. This script automates that process.

### ✨ How It Works

The script's logic is straightforward and effective:

> It takes the **filename stem** (the name without the extension) from the `source` folder and combines it with the **extension** from the `target` folder.

This operation is performed based on the alphabetically sorted order of files in both directories, ensuring a predictable pairing.

### 🚀 Features

* **Name Syncing:** Synchronizes filenames between two directories.
* **Extension Preservation:** Intelligently keeps the original file extensions in the target folder. This is its key feature.
* **Safe Operation:** Only renames as many files as are available in the smaller of the two folders to prevent errors.
* **Clear Logging:** Prints every single rename operation to the console so you can see exactly what's happening.
* **Robust Error Handling:** Gracefully handles issues like missing folders.

### 🔧 How to Use

**⚠️ IMPORTANT: Always create a backup of your target folder before running this script. The renaming operation is irreversible.**

1.  Open the script (`your_script_name.py`) in any code editor.
2.  Navigate to the bottom of the file, inside the `if __name__ == "__main__":` block.
3.  Modify the `source` and `target` variables to point to your actual folder paths:

    ```python
    # Example usage:
    if __name__ == "__main__":
        source = "path/to/your/source_folder_with_good_names"
        target = "path/to/your/target_folder_to_be_renamed"

        rename_files(source, target)
    ```

4.  Save the file and run it from your terminal:

    ```bash
    python your_script_name.py
    ```

#### Example Output:

```
Renamed: DOC001.pdf -> Project_Report_Final.pdf
Renamed: sheet_v2.csv -> Data_Analysis.csv
Renamed: slides_draft.key -> Presentation_Slides.key

Total files renamed: 3/3
```

### 📜 License

This project is licensed under the MIT License.
