import boto3
from botocore.config import Config

def get_boto_client(aws_config, profile="default"):
    boto3.setup_default_session(profile_name=profile)
    return boto3.client('codeartifact', config=aws_config)

def get_codeartifact_client(args, source=True):
    aws_config = Config(
        region_name=args.codeartifactregion,
        signature_version='v4',
        retries={
            'max_attempts': 10,
            'mode': 'standard'
        }
    )
    if source:
        return get_boto_client(aws_config, profile=args.source_profile)
    return get_boto_client(aws_config, profile=args.destination_profile)