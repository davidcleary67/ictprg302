#!/usr/bin/python3

import sys
import os
import pathlib
import shutil
import smtplib
from datetime import datetime
from backupcfg import jobs, dstPath, logPath, smtp

def sendEmail(message):

    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")


def logging(errorMessage):
    try:
        file = open(logPath, "a")
        file.write(f"FAILURE {errorMessage}\n")
        file.close()
    
    except FileNotFoundError:
        print("ERROR: File does not exist.")
    except IOError:
        print("ERROR: File is not accessible.")

def error(errorMessage, dateTimeStamp):
    print(errorMessage)
    logging(errorMessage)
    sendEmail(errorMessage)
    # write failure to log
    # email message
    
def main():
    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    argCount = len(sys.argv)
    if argCount != 2:
        error("ERROR: jobname missing from command line", dateTimeStamp)
    else:
        jobName = sys.argv[1]
        if jobName not in jobs:
            error(f"ERROR: jobname {jobName} not defined.", dateTimeStamp)
        else:
            srcPath = jobs[jobName]
            if not os.path.exists(srcPath):
                error(f"ERROR: Source path {srcPath} does not exist.", dateTimeStamp)    
            else:
                if not os.path.exists(dstPath):
                    error(f"ERROR: Destination path {dstPath} does not exist.", dateTimeStamp)
                else:
                    srcDetails = pathlib.PurePath(srcPath)
                    dstLoc = f"{dstPath}/{srcDetails.name}-{dateTimeStamp}"
                    
                    if pathlib.Path(srcPath).is_dir():
                        shutil.copytree(srcPath, dstLoc)
                    else:
                        shutil.copy2(srcPath, dstLoc)
                        
                    # write SUCCESS to log file

if __name__ == "__main__":
    main()