import boto3


def upload_file(file_name, s3_key):
    """Uploads existing file to 'gthomakos14-statcast' bucket

    Parameters
    ----------
        file_name : str
            The fully qualified name of the file to be uploaded

        s3_key : str
            The unique name of the file in the s3 bucket
    """

    s3_client = boto3.client('s3', region_name='us-east-2')
