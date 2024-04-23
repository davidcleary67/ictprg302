jobs = {'job17':'/home/ec2-user/environment/ictprg302/file1.dat',
        'job18':'/home/ec2-user/environment/ictprg302/dir1'}
        
dstPath = '/home/ec2-user/environment/ictprg302/backups'

logPath = '/home/ec2-user/environment/ictprg302/backup.log'

smtp = {"sender": "davidcgcleary@gmail.com",    # elasticemail.com verified sender
        "recipient": "dcleary@sunitafe.edu.au", # elasticemail.com verified recipient
        "server": "smtp.elasticemail.com",      # elasticemail.com SMTP server
        "port": 2525,                           # elasticemail.com SMTP port
        "user": "davidcgcleary@gmail.com",      # elasticemail.com user
        "password": "AAAABBBBXXXXYYYYZZZZ"}     # elasticemail.com password