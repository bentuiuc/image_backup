from pathlib import Path

def split_to_batch(p: str = '..', batch_size: int = 30):
    files_location = Path(p)    # the files path
    files = files_location.glob('*.*')
    files_filename_list = [f for f in files] # list of file names
    
    # return if file count is not big enough
    if len(files_filename_list) <= batch_size:
        print(f'file count <= batch size, not batching required')
        return
    
    batched_files = [files_filename_list[x:x+batch_size] for x in range(0, len(files_filename_list), batch_size)] # split the filename into batches

    # make folders & move files
    for i in range(len(batched_files)):
        folder_name = f'/Batch{i}'
        dir_path = Path(p + folder_name)
        dir_path.mkdir(exist_ok=True)

        for curr_file in batched_files[i]:
            curr_file.rename(dir_path / curr_file.name)


if __name__ == "__main__":
    split_to_batch()

