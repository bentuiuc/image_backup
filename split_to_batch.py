from pathlib import Path

def split_to_batch(p: str = '..', batch_size: int = 30):
    files_location = Path(p)    # the files path
    files_filename = [f for f in files_location.iterdir()] # list of file names
    
    # return if file count is not big enough
    if len(files_filename) <= batch_size:
        print(f'file count <= batch size, not batching required')
        return
    
    batched_files = [files_filename[x:x+batch_size] for x in range(0, len(files_filename), batch_size)] # split the filename into batches
    files_location.mkdir()


if __name__ == "__main__":
    split_to_batch()

