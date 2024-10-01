from faker import Faker
from .constants import standard_values, sql_table_structures
import random
import re
import string

def generate_data(table_name, record_count):

    fake = Faker()
    data = []
    try:
        if table_name not in sql_table_structures.keys():
            raise Exception("Invalid table name")

        table_columns = sql_table_structures[table_name]
        for _ in range(record_count):
            record = {}
            for col, col_props in table_columns.items():
                # Skip the identity value
                if col_props["is_identity"]:
                    continue

                # foreign key value
                elif '_fk' in col.lower():
                    record[col] = fake.random_int(min=1, max=1000000)
                
                elif col == "md_process_identifier":
                    record[col] = fake.uuid4()
                
                # standard values
                elif col in standard_values.keys():
                    if isinstance(standard_values[col], str):
                        record[col] = standard_values[col]
                    elif isinstance(standard_values[col], list):
                        length_of_list = len(standard_values[col])
                        record[col] = standard_values[col][fake.random_int(min=0, max=length_of_list-1)]
                
                elif col_props["datatype"] == "bigint":
                    record[col] = fake.random_int(min=1, max=2**63-1)

                elif col_props["datatype"] == "bit":
                    record[col] = fake.boolean()

                elif col_props["datatype"] == "date":
                    record[col] = fake.date(pattern="%Y-%m-%d")

                elif col_props["datatype"] == "datetime":
                    record[col] = fake.date_time().strftime('%Y-%m-%d %H:%M:%S.') + str(fake.random_int(min=0, max=999)).zfill(3)

                elif col_props["datatype"] in ('decimal(13, 2)', 'decimal(20, 2)'):
                    if '_percentage' in col.lower() or 'percentage_' in col.lower() or '_percentage_' in col.lower():
                        record[col] = fake.pydecimal(left_digits=(2, 3), right_digits=2, max_value=100.00, positive=True)
                    elif '_weight' in col.lower() or 'weight_' in col.lower() or '_weight_' in col.lower():
                        record[col] = fake.pydecimal(left_digits=(1, 4), right_digits=2, positive=True)
                    elif '_number' in col.lower() or 'number_' in col.lower() or '_number_' in col.lower():
                        record[col] = round(fake.random_int(min=1000, max=10000000, step=1))
                    else:
                        record[col] = fake.pydecimal(left_digits=(2,4), right_digits=2, positive=True)

                elif col_props["datatype"] == "int":
                    record[col] = fake.random_int(min=1, max=2**31-1)

                elif col_props["datatype"] in ('nchar(1)', 'nvarchar(1)'):
                    record[col] = fake.random_letter()
                                
                elif col_props["datatype"] in ('nvarchar(2)', 'varchar(2)'):
                    record[col] = ''.join(fake.random_choices(elements='ABCDEFGHIJKLMNOPQRSTUVWXYZ', length=2))

                elif col_props["datatype"] in ('nvarchar(max)', 'varchar(max)'):
                    record[col] = fake.text()

                elif "nvarchar" in col_props["datatype"] or "varchar" in col_props["datatype"]:
                    if '_te_id' in col.lower():
                        record[col] = 'TE-'+str(fake.random_int(min=1000000, max=9999999))
                    elif '_number' in col.lower() or 'number_' in col.lower() or '_number_' in col.lower():
                        record[col] = str(round(fake.random_int(min=1000, max=10000000, step=1)))
                    else:
                        max_chars = int(re.search(r'\d+', col_props["datatype"]).group())
                        if '_no_' in col.lower() or '_no' in col.lower() or 'no_' in col.lower():
                            record[col] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(max(20, max_chars)))
                        else:
                            record[col] = fake.text(max_nb_chars=max_chars)
            
            data.append(record)
        return data
    
    except Exception as e:
        raise Exception(str(e))
    
