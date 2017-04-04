#!/usr/bin/env python3
'''
Suppose you have a s3 bucket named bucketname
and have a folder inside that bucket named dir_name.
The list of files are either in your csv/text file.
Tweak it according to your  need.

'''
import logging
from boto.s3.connection import S3Connection


AWS_KEY = ''
AWS_SECRET = ''
aws_connection = S3Connection( AWS_KEY, AWS_SECRET )
bucket = aws_connection.get_bucket( "bucketname" )
'''
use this if you only want to download files from directory called dir_name
for multiple folders , give name seprated by comma.
 bucket.list() - for downloading from root directory
 bucket.list("dir_name", "/")
'''
for key in bucket.list("dir_name"):
    with open( "s3down.txt", "r" ) as f:
        lines = [line.rstrip( '\n' ) for line in open( 's3down.txt' )]
        for elem in lines:
            fname="dir_name"+"/"+str(elem)
            if fname==key.name:
                try:
                    res = key.get_contents_to_filename(str(key.name).replace('/', '_'))
                    print ("Downloading",(key.name))
                except:
                    logging.info( key.name + ":" + "not in bucket" )
