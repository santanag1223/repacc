# pacc.py - script heals .lil.bin files from TargetBins folder and breaks them into
#            500MB chuncks to be shared over discord.

import os

os.makedirs('../pacced/', exist_ok=True)

# Change to the repacced directory
os.chdir('../repacced/')
for repaccedFolder in os.listdir():
    # create a new bin file to write the lil.bin files to
    paccingBin = open(f"../pacced/{repaccedFolder}.bin", 'wb')
    # change dirs to repaccedFolder in repacced
    os.chdir(repaccedFolder)
    # iterate through all lil.<index>.bin files in the repaccedFolder
    for i in range(len(os.listdir())):
        try:
            if f'{repaccedFolder.removesuffix('.bin')}.lil.{i}.bin' not in os.listdir():
                print(f'{repaccedFolder.removesuffix('.bin')}.lil.{i}.bin MISSING in {repaccedFolder}')
                break
            with open(f'{repaccedFolder.removesuffix('.bin')}.lil.{i}.bin', 'rb') as currLil:
                bytes = currLil.read()
                paccingBin.write(bytes)
        except Exception as e:
            print("------------------------------------")
            print(f'Error while reading lil.{i}.bin :\n{e}')
            break
    # change dirs back to repacced, out of repaccedFolder
    os.chdir('..')
    # close the newly pacced bin file
    paccingBin.close()
    print(f'{paccingBin.name} pacced.')