import boto3

client = boto3.client('ecr')

repository_name = "cloudnative-monitoring"
response = client.create_repository(repositoryName=repository_name)

if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print(f"ECR repository '{repository_name}' created successfully.")
else:
    print(f"Failed to create ECR repository '{repository_name}'.")

repository_url = response['repository']['repositoryUri']

print(repository_url)