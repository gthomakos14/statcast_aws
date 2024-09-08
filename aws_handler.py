import boto3
import s3fs


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


def upload_df(df, destination):
    """
    Sends polars df to s3 bucket as a parquet

    Parameters
    ----------
        df : polars.DataFrame
            The data frame to be sent up
        destination : str
            The fully qualified file name in s3 that the data frame will be stored as
    """
    fs = s3fs.S3FileSystem()
    with fs.open(destination, mode='wb') as output:
        df.write_parquet(output)
