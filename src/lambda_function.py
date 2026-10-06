import json

def lambda_handler(event, context):
    # TODO implement
    print("deploy lambda function using github cicd")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from (vscode to github)  Lambda!')
    }