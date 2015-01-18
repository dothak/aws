#!/usr/bin/env python

import boto
import boto.ec2
import string
import os
import sys
import time



A_KEY = os.getenv("aws_access_key_id")
S_KEY = os.getenv("aws_secret_access_key")

conn = boto.ec2
ec2_region_connect = conn.connect_to_region(sys.argv[1], aws_access_key_id=A_KEY, aws_secret_access_key=S_KEY)



#Get the attach data so we can see what instances the volumes are attached to
#Printing a returns multiple instances because there can be more than 1 volume
#attached to an instance
for a in ec2_region_connect.get_all_volumes():
    attachmentset = a.attach_data
    instance_id = attachmentset.instance_id
    print 'Working on instance id %s ' % instance_id
    time.sleep(30)
    print "sleeping 30"

    if instance_id:
        for id in ec2_region_connect.get_only_instances(instance_id):
            if id.tags.has_key('xxxx'):
                a.add_tag('xxxx', value=id.tags['xxxx'])
                print 'Instance id: %s has customer id: %s ' % (instance_id, id.tags['xxxx'])
                print 'Added tag: %s to volume: %s ' % (id.tags['xxxx'], a)

            else:
                print 'No tag of cust-id for instance: %s' % instance_id
            if id.tags.has_key('xxxx'):
                a.add_tag('xxxx', value=id.tags['xxxx'])
                print 'Instance id: %s has name: %s ' % (instance_id, id.tags['xxxx'])
                print 'Added tag %s to volume %s ' % (id.tags['xxxx'], a)

            else:
                print "xxxx already set to ", id, a
    else:
        print "no instanced attached"
