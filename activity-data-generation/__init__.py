# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from shared.blob import write_to_file
from shared.utils import generate_data
import json
import io
import csv
import os

def main(result):
    try:
        data = json.loads(result)
        table_name = data["table_name"]
        batch = data["batch"]
        batch_size = data["batch_size"]

    except Exception as e:
        return json.dumps(
            { 
                "status_code": 400,
                "message": str(e)
            }
        )
    
    try:
        data = generate_data(table_name, batch_size)

        output = io.StringIO()
        # Write the data to the CSV in-memory
        writer = csv.DictWriter(output, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        
        # Get the content of the CSV as bytes
        csv_data = output.getvalue().encode('utf-8')
        
        # Write to Azure Blob Storage using the provided function
        write_to_file(
            connection=os.getenv("BLOB_CONNECTION_STRING"),
            container=os.getenv("BLOB_CONTAINER"),
            filename=f"{table_name}/{table_name}_{batch}.csv",
            content=csv_data
        )
    except Exception as e:
        return json.dumps(
            { 
                "status_code": 400,
                "message": str(e)
            }
        )
    
    logging.info(f"Generated batch-{batch} for table {table_name}")

    return json.dumps(
            { 
                "status_code": 200,
                "message": f"Batch-{batch} for table {table_name} generated successfully"
            }
        )
    


    