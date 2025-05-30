import os
from datetime import datetime
from PyPDF2 import PdfMerger
import argparse

def merge_pdfs_by_date(folder_path, output_filename="merged_pdfs.pdf"):
    """
    Merge all PDFs in a folder from oldest to newest based on file modification time.
    
    Args:
        folder_path (str): Path to the folder containing PDF files
        output_filename (str): Name of the output merged PDF file
    """
    
    # Get all PDF files in the folder
    pdf_files = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            # Get modification time
            mod_time = os.path.getmtime(file_path)
            pdf_files.append((file_path, mod_time, filename))
    
    if not pdf_files:
        print("No PDF files found in the specified folder.")
        return
    
    # Sort by modification time (oldest first)
    pdf_files.sort(key=lambda x: x[1])
    
    # Create PdfMerger object
    merger = PdfMerger()
    
    print(f"Found {len(pdf_files)} PDF files. Merging in chronological order:")
    
    try:
        # Add each PDF to the merger
        for file_path, mod_time, filename in pdf_files:
            print(f"Adding: {filename} (Modified: {datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')})")
            merger.append(file_path)
        
        # Write the merged PDF
        output_path = os.path.join(folder_path, output_filename)
        with open(output_path, 'wb') as output_file:
            merger.write(output_file)
        
        print(f"\n✅ Successfully merged {len(pdf_files)} PDFs into: {output_path}")
        
    except Exception as e:
        print(f"❌ Error during merging: {str(e)}")
    
    finally:
        merger.close()

def main():
    parser = argparse.ArgumentParser(description="Merge PDF files from oldest to newest")
    parser.add_argument("folder", help="Path to folder containing PDF files")
    parser.add_argument("-o", "--output", default="merged_pdfs.pdf", 
                       help="Output filename (default: merged_pdfs.pdf)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.folder):
        print(f"❌ Error: Folder '{args.folder}' does not exist.")
        return
    
    merge_pdfs_by_date(args.folder, args.output)

if __name__ == "__main__":
    main()