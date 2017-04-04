#!/usr/bin/env python3
'''
use this if all your files are in your root directory.
Tweak the file name list according to your need.
'''
import logging
from boto.s3.connection import S3Connection


AWS_KEY = ''
AWS_SECRET = ''
aws_connection = S3Connection( AWS_KEY, AWS_SECRET )
bucket = aws_connection.get_bucket( "bucketname" )

for key in bucket.list():
    with open( "s3down.txt", "r" ) as f:
        lines = [line.rstrip( '\n' ) for line in open( 's3down.txt' )]
        for elem in lines:
            if elem==key.name:
                try:
                    res = key.get_contents_to_filename(key.name)
                    print ("Downloading",(key.name))
                except:
                    logging.info( key.name + ":" + "not in bucket" )
