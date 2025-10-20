import boto3

# Inisitalize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference the existing table
table = dynamodb.Table('user-table')

# Insert items into the table
item1 = {
    'user_id': '001',
    'name': 'Alice',
    'age': 30,
}

response1 = table.put_item(Item=item1)
print('Inserted item:', response1)

# Insert second item
item2 = {
    'user_id': '002',
    'name': 'Bob',
    'age': 25,
}

response2 = table.put_item(Item=item2)
print('Inserted item:', response2)
