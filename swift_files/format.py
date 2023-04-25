'''

- this script should take an excel file and remove duplicates and generate a report

- Read the file
- Find the duplicates (by scanning the rows, there might be a pd method for this.)
- If there are duplicates move them to the bottom of the sheet, highlight the duplicates row in red. 

'''

import pandas as pd

def read_data(path, sheet_name=0):
    data_frame = pd.read_excel(path, sheet_name)
    return data_frame
    