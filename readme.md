# merge_pdfs.py

## Description

This Python script merges all PDF files found within a specified folder. The PDFs are merged in chronological order based on their last modification time, from oldest to newest. The merged output is saved as a new PDF file.

## Prerequisites

Before running this script, ensure you have the following installed:

*   **Python**: Version 3.7+ (recommended)
*   **Required Libraries**:
    *   `PyPDF2`

    You can typically install these libraries using pip:
    ```bash
    pip install PyPDF2

    ```
    Or, if a `requirements.txt` file is provided:
    ```bash
    pip install -r requirements.txt
    ```
 *(Note: A `requirements.txt` file is not currently provided with this script, so direct installation of `PyPDF2` is recommended.)*


## Usage

To run the script, use the following command structure from your terminal:

```bash
python merge_pdfs.py <folder_path> -o <output_file_name>
```

## Examples

Provide a few examples of how to use the script with different parameters.

1.  **Basic Usage:**
    ```bash
    python merge_pdfs.py ./pdfs -o merged.pdf
    ```

