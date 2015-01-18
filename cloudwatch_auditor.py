#!/usr/bin/env python

import boto
import boto.ec2
import boto.ec2.cloudwatch
import boto.sns

import string
import os
import sys
import re
import csv
import json
import ConfigParser
import time



home = os.path.expanduser("~")
file_path = "%s/.aws/profile" % home
cp = ConfigParser.ConfigParser()

cp.read(file_path)

for section in cp.sections():
        for name, value in cp.items(section):
            if name == 'aws_access_key_id':
                 os.environ['aws_access_key_id'] = value
                 A_KEY = os.environ['aws_access_key_id']
            elif name == 'aws_secret_access_key':
                os.environ['aws_secret_access_key'] = value
                S_KEY = os.environ['aws_secret_access_key']
                ec2_conn = boto.ec2.EC2Connection(A_KEY, S_KEY)
                region = ec2_conn.get_all_regions()
                for acct_id in ec2_conn.get_all_security_groups(groupnames='default'):
                    aws_account_id = acct_id.owner_id

        for r in boto.ec2.cloudwatch.regions():
            if r.name == 'us-gov-west-1' or r.name == 'eu-central-1' or r.name == 'cn-north-1':
                continue

            cw = boto.connect_cloudwatch(A_KEY, S_KEY, region=r)
            derp = cw.describe_alarms()
            if derp.next_token:
                for things in derp:
                    print "Name: %s \t Metric: %s \t Alarm Action: %s" % (things.name, things.metric, things.alarm_actions)
            else:
                print "Name: %s \t " % things.alarm_actions
