import pandas as pd

def gen_sql_type(pd_type):

    sql_type = ""

    if "string" in pd_type.lower():
        sql_type = "VARCHAR"

    if "int" in pd_type.lower():
        sql_type = "INT"

    if "float" in pd_type.lower():
        sql_type = "FLOAT"

    return sql_type

def get_type_dict(file_name):

    df = pd.read_csv(file_name)

    type_dict = {}

    for i in range(len(df.columns)):
        type_dict[df.columns[i]] = gen_sql_type(str(df.convert_dtypes().dtypes[i]))

    return type_dict