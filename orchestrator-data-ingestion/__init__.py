# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json
from shared.constants import sql_table_structures

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    first_retry_interval_in_milliseconds = 300000
    max_number_of_attempts = 3
    retry_options = df.RetryOptions(
        first_retry_interval_in_milliseconds, max_number_of_attempts
    )

    data = context.get_input()
    table_name = data.get("table_name", None)
    total_records = data.get("total_records", None)
    batch_size = data.get("batch_size", None)
    tasks = []

    if not (table_name or total_records or batch_size):
        result = json.dumps(
            {"status": False, "message": "table_name, total_records or batch_size is missing"}
        )
        return result
    
    if table_name not in sql_table_structures.keys():
        result = json.dumps(
            {"status": False, "message": f"Invalid table name '{table_name}'"}
        )
        return result
    
    logging.info(f"Starting activity-data-generation")
    for batch in range(0,  total_records, batch_size):
        data["batch"] = int(batch/batch_size)+1
        tasks.append(
            # context.call_activity_with_retry(
            #     name='activity-data-generation', 
            #     retry_options=retry_options, 
            #     input_=json.dumps(data)
            # )
            context.call_activity(
                name='activity-data-generation', 
                input_=json.dumps(data)
            )
        )
        # logging.info(f"Running activity-data-generation for batch-{batch+1}/{int(total_records/batch_size)}")

    results = yield context.task_all(tasks)
    return results

    # result1 = yield context.call_activity('Hello', "Tokyo")
    # result2 = yield context.call_activity('Hello', "Seattle")
    # result3 = yield context.call_activity('Hello', "London")
    # return [result1, result2, result3]

main = df.Orchestrator.create(orchestrator_function)