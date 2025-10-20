import boto3

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Create table
table_name = 'user-table'

table = dynamodb.create_table(
    TableName = table_name,
    KeySchema = [
        {
            'AttributeName': 'user_id',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'user_id',
            'AttributeType': 'S'  # String type
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print(f'Creating table {table_name}...')
table.wait_until_exists()
print(f'Table {table_name} created successfully.')