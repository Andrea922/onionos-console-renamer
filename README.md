# Onion OS Console Renamer
A little script written in Python that allows you to rename as many consoles at once!
It was specifically written for [Onion OS](https://github.com/OnionUI).

## Usage
0. Backup your Emu folder, first!
1. Download the [zip file](https://github.com/Andrea922/onionos-console-renamer/archive/refs/heads/master.zip)
2. Extract the `onionos-console-renamer-master` folder in the Emu folder of your Onion OS
3. Run the `get.bat` (or `python py/get.py`) to get the console names
4. A `data.xlsx` file will be generated in the root of `onionos-console-renamer-master` folder; there, in the New_label column you will set the new names for the consoles; leave blank where not needed
5. Save and close the `data.xlsx` file
6. Run the `set.bat` (or `python py/set.py`) to update the console names!
