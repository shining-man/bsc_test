import os
import subprocess
import sys
from pathlib import Path
import time

# Configuration - Define translation jobs here
# Each job specifies source directories and a target directory
TRANSLATION_JOBS = [
    {
        "source_dirs": ["docs"],  # Source directories to translate
        "target_dir": "docs/en"    # Target directory for translated files
    }
    # You can add more jobs as needed, for example:
    #{
    #    "source_dirs": ["docs/", "content/de"],  # Source directories to translate
    #    "target_dir": "translated"                     # Target directory for translated files
    #}
    
    # {
    #     "source_dirs": ["another/german/folder"],
    #     "target_dir": "another/translated/folder" 
    # }
]

# Path to the translator script
TRANSLATOR_SCRIPT = "md_translate.py"  # The script we just created

def translate_job(job):
    """
    Processes all markdown files in the source directories and translates them to the target directory
    """
    source_dirs = job["source_dirs"]
    target_dir = job["target_dir"]
    
    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    total_files = 0
    processed_files = 0
    
    # Process each source directory
    for source_dir in source_dirs:
        source_path = Path(source_dir)
        
        # Check if source directory exists
        if not source_path.exists() or not source_path.is_dir():
            print(f"Warning: Source directory not found: {source_dir}")
            continue
        
        print(f"\nProcessing directory: {source_dir}")
        
        # Find all markdown files in the source directory and subdirectories
        md_files = list(source_path.glob("**/*.md"))
        total_files += len(md_files)
        
        if not md_files:
            print("No markdown files found.")
            continue
        
        print(f"Found {len(md_files)} markdown files")
        
        # Process each markdown file
        for i, md_file in enumerate(md_files, 1):
            # Calculate the relative path from the source directory
            rel_path = md_file.relative_to(source_path)
            
            # Create the target path in the target directory
            target_file = Path(target_dir) / rel_path
            
            # Create parent directories if they don't exist
            os.makedirs(target_file.parent, exist_ok=True)
            
            print(f"[{i}/{len(md_files)}] Translating: {rel_path}")
            
            # Call the translator script
            cmd = [
                sys.executable,
                TRANSLATOR_SCRIPT,
                str(md_file),
                "-o",
                str(target_file)
            ]
            
            try:
                subprocess.run(cmd, check=True)
                print(f"  ✓ Translated to {target_file}")
                processed_files += 1
            except subprocess.CalledProcessError as e:
                print(f"  ✗ Error translating {md_file}: {e}")
    
    return processed_files, total_files

def main():
    # Check if translator script exists
    if not os.path.exists(TRANSLATOR_SCRIPT):
        print(f"Error: Translator script not found: {TRANSLATOR_SCRIPT}")
        return False
    
    start_time = time.time()
    
    print("Starting batch translation of markdown files...")
    
    total_processed = 0
    total_files = 0
    
    # Process each translation job
    for i, job in enumerate(TRANSLATION_JOBS, 1):
        print(f"\nJob {i}/{len(TRANSLATION_JOBS)}")
        print(f"Source directories: {job['source_dirs']}")
        print(f"Target directory: {job['target_dir']}")
        
        processed, files = translate_job(job)
        total_processed += processed
        total_files += files
    
    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    
    print(f"\nBatch translation completed in {int(minutes)} minutes and {seconds:.1f} seconds.")
    print(f"Files processed: {total_processed}/{total_files}")

if __name__ == "__main__":
    main()