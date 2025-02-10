import os
import zipfile
import shutil

def setup_data_directory():
    """Create data directory if it doesn't exist."""
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')
    os.makedirs(data_dir, exist_ok=True)
    return data_dir

def extract_wine_data():
    """Extract wine quality data from downloaded zip file."""
    downloads_dir = os.path.expanduser('~/browser_downloads')
    zip_path = os.path.join(downloads_dir, 'wine+quality.zip')
    data_dir = setup_data_directory()
    
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Downloaded zip file not found at {zip_path}")
        
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(data_dir)
    
    print(f"Data files extracted to {data_dir}")
    return data_dir

if __name__ == '__main__':
    extract_wine_data()
