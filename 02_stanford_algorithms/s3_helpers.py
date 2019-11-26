from boto.s3.connection import S3Connection
from boto.s3.key import Key
import os
import pickle


def get_s3_bucket(bucket_name):
    """
    Get an S3 bucket from the bucket name.
    param: bucket name
    """
    conn = S3Connection(os.environ["AWS_ACCESS_KEY"], os.environ["AWS_SECRET_KEY"])
    bucket = conn.get_bucket(bucket_name)
    return bucket


def add_object_to_bucket(bucket, key_name, object_to_upload):
    """
    Add an object to an S3 bucket.
    param: bucket: the s3 bucket object
    param: key_name: a string that represents the key name that will be stored
    param: object: the python object that you want to assign to that key
    """
    pickle.dump(object_to_upload, open("./temp.p", "wb"))
    k = Key(bucket)
    k.key = key_name
    k.set_contents_from_filename("./temp.p")
    return None


def get_object_from_bucket(bucket, key_name):
    """
    Add an object to an S3 bucket.
    param: bucket: the s3 bucket object
    param: key_name: a string that represents the key name that will be stored

    returns: object from s3 bucket
    """
    k = Key(bucket)
    k.key = key_name
    k.get_contents_to_filename("./temp.p")
    new_object = pickle.load(open("./temp.p", "rb"))
    return new_object
