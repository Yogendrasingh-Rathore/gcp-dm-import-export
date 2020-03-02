import sys
import os


def read_acl():
    try:
        SERVICE_ACCOUNT_ADDRESS = raw_input("Enter Service Account :  ")  
        BUCKET_NAME = raw_input("Enter Bucket Name :  ")
        sqldumpfileName = raw_input("Enter Object Name :  ")
        Extention = raw_input("Enter Object Extention :  ")

        acl_cmd = 'gsutil acl ch -u {0}:R gs://{1}/{2}.{3}'.format(SERVICE_ACCOUNT_ADDRESS, BUCKET_NAME, sqldumpfileName, Extention)
        print("Adding READ Permission")
        os.system(acl_cmd)
    except Exception as e:
      print(str(e))
      print("Exception in updating read acl")


def write_acl():
    try:
        SERVICE_ACCOUNT_ADDRESS = raw_input("Enter Service Account :  ")  
        BUCKET_NAME = raw_input("Enter Bucket Name :  ")
        
        acl_cmd = 'gsutil acl ch -u {0}:W gs://{1}'.format(SERVICE_ACCOUNT_ADDRESS, BUCKET_NAME)
        print("Adding WRITE Permission")
        os.system(acl_cmd)
    except Exception as e:
      print(str(e))
      print("Exception in updating write acl")

def update_dm():
    try:
        choice = raw_input("1.Import Data from Bucket\n2.Export Data to Bucket\nEnter your choice:  ")
        if choice == '1':
            read_acl()
        elif choice == '2':
            write_acl()
        else:
            print("Invalid Choice!")

        deployment_name = raw_input('Enter Deployment Name: ')
        template_fileName = raw_input('Enter Template File Name: ')
        template_filePath = os.getcwd() + '/Tmpl/' + template_fileName + '.tmpl'
        config_fileName = template_fileName + '.yaml'
        os.system('envsubst < {0} > {1}'.format(template_filePath, config_fileName))
        deployment_manager_cmd = 'gcloud deployment-manager deployments \
                                update {0} --config {1} '.format(
                                deployment_name, config_fileName)
        os.system(deployment_manager_cmd)
    except Exception as e:
        print(str(e))
        print("Exception in updating SQL INSTANCE")


update_dm()
