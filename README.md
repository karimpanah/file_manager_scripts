# 🔀 Batch File Renamer

A simple yet powerful Python script to rename files in a target folder based on the filenames in a source folder, while intelligently preserving the original file extensions.

---

### 🤔 What's the Problem?

Ever had two folders of related files with inconsistent naming?
* `Folder A` (Source): `Project_Report_Final.txt`, `Data_Analysis.xlsx`, `Presentation_Slides.pptx`
* `Folder B` (Target): `DOC001.pdf`, `sheet_v2.csv`, `slides_draft.key`

You want the files in `Folder B` to match the names from `Folder A`, but keep their original extensions (`.pdf`, `.csv`, `.key`). Doing this manually for hundreds of files is a nightmare. This script automates that nightmare away.

### ✨ How It Works

The script operates on a simple, powerful principle:

> It takes the **filename (without extension)** from the `source` folder and combines it with the **extension** from the `target` folder.

This is done based on the alphabetically sorted order of files in both directories.

### 🚀 Features

* **Name Syncing:** Synchronizes filenames between two directories.
* **Extension Preservation:** Never alters the original file extensions in the target folder.
* **Safe Operation:** Only renames as many files as are available in the smaller of the two folders.
* **Clear Logging:** Prints every rename operation to the console for full transparency.
* **Robust Error Handling:** Built to handle missing folders and other potential issues gracefully.

### 🔧 Getting Started

This script requires **Python 3.6+** (due to `pathlib`). No external libraries are needed.

1.  Clone this repository or download the `batch_file_renamer.py` script.
2.  Place your source and target folders where you can easily access them.

### 💡 Usage

**⚠️ IMPORTANT: Always back up your target folder before running this script. The renaming operation is irreversible.**

1.  Open the script (`batch_file_renamer.py`) in a text editor.
2.  Navigate to the bottom of the file, inside the `if __name__ == "__main__":` block.
3.  Modify these two lines to point to your folders:

    ```python
    # Example usage:
    if __name__ == "__main__":
        source = "path/to/your/source_folder_with_good_names"
        target = "path/to/your/target_folder_to_be_renamed"

        rename_files(source, target)
    ```

4.  Save the file and run it from your terminal:

    ```bash
    python batch_file_renamer.py
    ```

**Example Output:**

```
Renamed: DOC001.pdf -> Project_Report_Final.pdf
Renamed: sheet_v2.csv -> Data_Analysis.csv
Renamed: slides_draft.key -> Presentation_Slides.key

Total files renamed: 3/3
```

### 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
