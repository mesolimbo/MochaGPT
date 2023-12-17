import boto3
import csv
import sys


def read_csv(file_path):
    """
    Read data from a CSV file and return a list of dictionaries.
    """
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def transform_data(data):
    """
    Transform the data into the format suitable for DynamoDB.
    """
    transformed_data = []
    for row in data:
        transformed_row = {k: v for k, v in row.items() if v}  # Removing empty values
        transformed_data.append(transformed_row)
    return transformed_data


def load_data_to_dynamodb(table_name, data):
    """
    Load data into the DynamoDB table.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    with table.batch_writer() as writer:
        for item in data:
            writer.put_item(Item=item)


def main(file_path, table_name):
    # Read and transform data
    csv_data = read_csv(file_path)
    transformed_data = transform_data(csv_data)

    # Load data into DynamoDB
    load_data_to_dynamodb(table_name, transformed_data)

    print("Data loading complete.")


if __name__ == "__main__":
    # Check if all parameters are provided, otherwise raise an error
    if len(sys.argv) != 3:
        raise ValueError(
            "Expected two arguments: csv_path and db_table_name."
            "Usage: python script.py <csv_path> <db_table_name>"
        )

    # Get file path from command line argument
    csv_path = sys.argv[1]
    # Get table name from command line argument
    db_table_name = sys.argv[2]

    main(csv_path, db_table_name)
