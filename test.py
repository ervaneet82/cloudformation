import time
from ec2_metadata import ec2_metadata

with open('/home/ec2-user/result.txt','w+') as f:
    f.write(ec2_metadata.instance_id)
    f.write("Start : %s" % time.ctime())
    time.sleep(300)
    f.write("End : %s" % time.ctime())