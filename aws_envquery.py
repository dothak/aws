#!/usr/bin/env python
import boto
import boto.ec2
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
        conn = boto.ec2.EC2Connection(A_KEY, S_KEY)
        region = conn.get_all_regions()
        for acct_id in conn.get_all_security_groups(groupnames='default'):
            aws_account_id = acct_id.owner_id
            print aws_account_id
            file_name = 'aws_accounts.csv'
            with open(file_name, 'a') as fn:
                writer = csv.writer(fn, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for name in region:

                    conn = boto.ec2
                    ec2_region_connect = conn.connect_to_region(name.name, aws_access_key_id=A_KEY, aws_secret_access_key=S_KEY)
                    for instance_name in ec2_region_connect.get_all_instances():
                        for instance in instance_name.instances:

                                if instance.tags.has_key('xxxx') and instance.tags.has_key('xxxx'):
                                    data = ([aws_account_id, instance.region.name, instance.id, instance.tags['xxxx'], instance.tags['xxxx'], instance.state, instance.launch_time])
                                    writer.writerow(data)

                                elif instance.tags.has_key('xxxx') and instance.tags.has_key('xxxx'):
                                    data = ([aws_account_id, instance.region.name, instance.id, instance.tags['xxxx'], instance.tags['xxxx'], instance.state, instance.launch_time])
                                    writer.writerow(data)

                                elif instance.tags.has_key('xxxx') and not instance.tags.has_key('xxxx):
                                    data = ([aws_account_id, instance.region.name, instance.id, instance.tags['xxxx'], "missing xxxx" , instance.state, instance.launch_time])
                                    writer.writerow(data)

                                elif instance.tags.has_key('xxxx') and not instance.tags.has_key('xxxx'):
                                    data =([aws_account_id, instance.region.name, instance.id, instance.tags['xxxx'], 'missing xxxx', instance.state, instance.launch_time])
                                    writer.writerow(data)

                                elif not instance.tags.has_key('xxxx') and instance.tags.has_key('xxxx'):
                                    data = ([aws_account_id, instance.region.name, instance.id, 'missing xxxx', instance.tags['xxxx'], instance.state, instance.launch_time])
                                    writer.writerow(data)

                                elif not instance.tags.has_key('xxxx') and instance.tags.has_key('xxxx'):
                                    data = ([aws_account_id, instance.region.name, instance.id, 'missing xxxx', instance.tags['xxxx'], instance.state, instance.launch_time])
                                    writer.writerow(data)

                                else:
                                    data =([aws_account_id, instance.region.name, instance.id, 'missing xxxx', 'missing xxxx', instance.state, instance.launch_time])
                                    writer.writerow(data)
