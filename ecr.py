from collections.abc import Mapping, MutableMapping
import boto3

ecr_client = boto3.client('ecr')

repository_name = "flask-vocab-app"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)