import os

def clean_filenames(directory):
    os.chdir(directory)

    files = os.listdir()

    for file in files:
        index = file.split('_')[0]
        
        file_extension = file.split('.')[-1]
        
        new_name = f"{index}.{file_extension}"
        
        os.rename(file, new_name)
        print(f"Renamed {file} to {new_name}")

if __name__ == "__main__":
    directory = "train/with_mask"
    clean_filenames(directory)
