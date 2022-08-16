# Import all the relevant libraries, try downloading them if missing
import importlib,os

for pckgs in ['pandas','xlsxwriter','xlrd','json','openpyxl', 'shutup', 'glob']:
    try:
        importlib.import_module(pckgs)
    except (ImportError,ModuleNotFoundError):
        os.system("pip install " + pckgs)

import pandas as pd
import json
import shutup
import openpyxl
from glob import glob

shutup.please()


# Read data.xlsx if it exists
filename = "data.xlsx"
if os.path.exists(filename):
    print(filename,"found!")
    print("Proceeding...")
    df = pd.read_excel(filename)
    print("Excluding blank entries...")
    df = df[df['New_label'].notna()] # Get rid of empty values, the ones we are not going to update
    
    # Let's make sure there are actual entries to update, otherwise let's not waste time
    if len(df) > 0:
        print("Entries to update:",len(df))
        
        # Make lists out of them, for better loopability
        folders = list(df['Console_folder'])
        current_labels = list(df['Current_label'])
        new_labels = list(df['New_label'])
        
        # The core loop to read and replace current (old) values with new ones
        for n in range(len(current_labels)):
            print("\t-",current_labels[n],">",new_labels[n])
            config_dir = "../"+str(folders[n])+"/config.json"
            with open(config_dir) as f:
                data = json.load(f)

            data['label'] = new_labels[n]
            
            with open(config_dir, 'w') as f:
                json.dump(data, f, indent=2)
    else:
        print("No entries to update... Nothing to do here. :)")