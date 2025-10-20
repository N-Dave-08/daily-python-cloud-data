import boto3

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference the existing table
table = dynamodb.Table('user-table')

# Query an item from the table
reponse = table.query(
    KeyConditionExpression=boto3.dynamodb.conditions.Key('user_id').eq('001')
)

# Print result
items = reponse.get('Items', [])
print('Queried items:', items)