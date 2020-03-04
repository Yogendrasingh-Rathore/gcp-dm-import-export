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


def create_dm():
  try:
      deployment_name = raw_input('Enter Deployment Name: ')
      template_fileName = raw_input('Enter Template File Name: ')
      template_filePath = os.getcwd() + '/Tmpl/' + template_fileName + '.tmpl'
      config_fileName = template_fileName + '.yaml'
      os.system('envsubst < {0} > {1}'.format(template_filePath, config_fileName))
      choice = raw_input('1. Create New Deployment Manager\n2. Update Deployment Manager\nEnter your choice: ')
      if choice == '1':
          deployment_manager_cmd = 'gcloud deployment-manager deployments \
                                    create {0} --config {1} --automatic-rollback-on-error'.format(
                                    deployment_name, config_fileName)
      elif choice == '2':
          update_choice = raw_input('1. Import to SQL Instance\n2. Export to Cloud Storage\nEnter your Choice: ')
          if update_choice == '1':
              read_acl()
          elif update_choice == '2':
              write_acl()
          else:
              print('Invalid Choice!')
          deployment_manager_cmd = 'gcloud deployment-manager deployments \
                                update {0} --config {1} '.format(
                                deployment_name, config_fileName)
      else:
          print('Invalid Choice!')
      os.system(deployment_manager_cmd)
  except Exception as e:
      print(str(e))
      print("Exception in creating deployment manager")


def enable_gcloud_apis():
    try:
        gcloud_service_list = {'deploymentmanager.googleapis.com',
                                'sqladmin.googleapis.com',
                                'storage-api.googleapis.com',
                              }
        for each in gcloud_service_list:
            cmd = 'gcloud services enable {0}'.format(each)
            print(cmd)
            os.system(cmd)
    except Exception as e:
        print("Exception in enabling service")
    return True

api_enable_choice = raw_input("Do you want to enable Api's: ")
if api_enable_choice.lower() == 'yes' or api_enable_choice.lower() == 'y':
    enable_gcloud_apis()
create_dm()
