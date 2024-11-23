import urllib.request
import zipfile
import os

# Server URL for the file to download
SERVER_URL = 'https://icarus.cs.weber.edu/~hvalle/cs4580/data/seaborData.zip'

def download_file(url):
    """
    Download the file from the provided URL.
    """
    # Extract file name from the URL
    file_name = os.path.basename(url)

    # Download the file
    urllib.request.urlretrieve(url, file_name)
    print(f"'{file_name}' has been downloaded.")

    # Check if the file is a zip file and unzip if necessary
    if file_name.endswith('.zip'):
        print(f"'{file_name}' is a zip file. Unzipping...")
        extract_zip_file(file_name)
    else:
        print(f"'{file_name}' is not a zip file. No unzipping necessary.")

def extract_zip_file(file_name):
    """
    Unzip the file in the current working directory
    """
    if zipfile.is_zipfile(file_name):
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())
        print(f"'{file_name}' has been unzipped in the current directory.")
    else:
        print(f"'{file_name}' is not a valid zip file or it may be corrupted.")

def main():
    """
    Driver Function
    """
    # Download and unzip the file from the server
    download_file(SERVER_URL)

    print('Main Function complete.')

if __name__ == '__main__':
    main()
