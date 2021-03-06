import pandas as pd
import dateutil.parser

def get_type(val):
    
    try:
        dateutil.parser.parse(val)

    except:

        try:
            int(val)

        except:

            try:
                float(val)

            except:
                return "string"

            else:
                return "float64"

        else:
            return "Int64" 
            # The Int actually needs to be capitalized because converting nulls to int (lowercase) causes the data type to become float in astype()

    else:
        return "datetime64"

def convert_col_types(df):

    col_types = {}

    for col in df.columns:
        
        for cell in df[col]:

            try:
                col_type = get_type(cell)

            except:
                pass

            else:
                col_types[col] = col_type
                break

    return df.astype(col_types, copy = False)
