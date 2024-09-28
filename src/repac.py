# repac.py - script repacs bin files SRC_BINS folder and breaks them into
#            450MB chuncks (<originalbin>.lil.<index>.bin) to be shared over discord.
import os

def format_lil_filename(bin_file: str, lil_num: int) -> str:
    """Formats the lil filename."""
    return f'{bin_file.removesuffix(".bin")}.lil.{lil_num}.bin'

def repacc_binfile(input_file: str, max_chunk_size=450 * 1024 * 1024):
    """Splits a .bin file into smaller chunks of up to 450 MB."""
    with open(input_file, 'rb') as f:
        lil_num = 0
        while True:
            lil = f.read(max_chunk_size)  # Read up to 256 MB per (lil) chunks
            # if the lil is empty, we've reached the end of the file
            if not lil:
                break
            # Write each lil chuncks into a new .bin file
            lilfilename = format_lil_filename(input_file, lil_num)
            os.makedirs(f'../repacced/{input_file.removesuffix('.bin')}', exist_ok=True)
            with open(f'../repacced/{input_file.removesuffix('.bin')}/{lilfilename}', 'wb') as lilfile:
                lilfile.write(lil)
            print(f'repacced {lilfilename}')
            lil_num += 1
        print(f'{input_file} repacc DONE.')

# Change to the SRC_BINS directory

os.chdir('../SRC_BINS/')
for binFile in os.listdir():
    if not binFile.endswith('.bin'):
        continue
    
    repacc_binfile(binFile)