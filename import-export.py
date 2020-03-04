import sys
import os


def read_acl():
    try:
        SERVICE_ACCOUNT_ADDRESS = raw_input("Enter Service Account :  ")
        sqldumpfileName = raw_input("Enter Object Name :  ")
        Extention = raw_input("Enter Object Extention :  ")

        acl_cmd = 'gsutil acl ch -u {0}:R gs://{1}/{2}.{3}'.format(SERVICE_ACCOUNT_ADDRESS, os.environ['STORAGE_BUCKET'], sqldumpfileName, Extention)
        print("Adding READ Permission")
        print(acl_cmd)
        os.system(acl_cmd)
    except Exception as e:
      print(str(e))
      print("Exception in updating read acl")


def write_acl():
    try:
        SERVICE_ACCOUNT_ADDRESS = raw_input("Enter Service Account :  ")  
        print(os.environ['STORAGE_BUCKET'])
        acl_cmd = 'gsutil acl ch -u {0}:W gs://{1}'.format(SERVICE_ACCOUNT_ADDRESS, os.environ['STORAGE_BUCKET'])
        print("Adding WRITE Permission")
        os.system(acl_cmd)
    except Exception as e:
      print(str(e))
      print("Exception in updating write acl")

def import_to_SQLInstance():
    try:
        read_acl()
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


def export_to_bucket():
    try:
        write_acl()
        #sqldumpfileName = raw_input('Enter Dump File Name: ')
        sql_dump_path = "gs://" + os.environ['STORAGE_BUCKET'] + '/sqldump.sql'
        DATABASE_NAME = raw_input('Enter DATABASE NAME: ')
        cmd = 'gcloud sql export sql {0} {1} -d {2}'.format(
                os.environ['SQL_INSTANCE']+ '-master', sql_dump_path, DATABASE_NAME)
        print(cmd)
        os.system(cmd)
    except Exception as e:
        print(str(e))
        print("Exception in exporting the database")
    return True


choice = raw_input("1.Import Data from Bucket\n2.Export Data to Bucket\nEnter your choice:  ")
if choice == '1':
    import_to_SQLInstance()
elif choice == '2':
    export_to_bucket()
else:
    print("Invalid Choice!")
