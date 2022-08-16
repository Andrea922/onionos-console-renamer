# Import all the relevant libraries, try downloading them if missing
import importlib,os

for pckgs in ['pandas','xlsxwriter','xlrd','json', 'shutup', 'glob']:
    try:
        importlib.import_module(pckgs)
    except (ImportError,ModuleNotFoundError):
        os.system("pip install " + pckgs)

import pandas as pd
import json
import shutup
from glob import glob

shutup.please()


# Create empty lists to populate afterwards
folder_names = []
labels = []


# Read directories in Emu folder
emu_dirs = next(os.walk('..'))[1]

# Loop through them
for e in emu_dirs:
    config_dir = "../"+str(e)+"/config.json"
    exists = os.path.exists(config_dir)
    if exists:
        json_string = open(config_dir, "r")
        parsed = json.loads(json_string.read())
        labels.append(parsed['label'])
        folder_names.append(e)
        
        # Printing some output
        print(e,">",parsed['label'])

# Create Excel file
filename = "data.xlsx"
df = pd.DataFrame(data={"Console_folder": folder_names, "Current_label":labels})
df.insert(2, "New_label", "") 
print("\n\nCreating data file...")
df.to_excel(filename, index=None)
print(filename,"created")