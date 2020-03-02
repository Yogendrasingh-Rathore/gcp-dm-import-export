import sys
import os

def create_sqlInstance():
  try:
      deployment_name = raw_input('Enter Deployment Name: ')
      template_fileName = raw_input('Enter Template File Name: ')
      template_filePath = os.getcwd() + '/Tmpl/' + template_fileName + '.tmpl'
      config_fileName = template_fileName + '.yaml'
      #config_filePath = os.getcwd() + '/Yaml/' + config_fileName
      os.system('envsubst < {0} > {1}'.format(template_filePath, config_fileName))
      deployment_manager_cmd = 'gcloud deployment-manager deployments \
                                create {0} --config {1} '.format(
                                deployment_name, config_fileName)
      os.system(deployment_manager_cmd)
  except Exception as e:
      print(str(e))
      print("Exception in creating SQL INSTANCE")


create_sqlInstance()
