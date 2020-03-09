# gcp-dm-import-export

Here the AIM is to achieve:

i. Create the SQL Instance

ii. Export the data from SQL Instance to the Cloud Storage Bucket

iii. Then from that dump file create a new SQL Instance(Import)

All this must be done using the GCP Deployment Manager

The Approach Followed is:

i. Jinja Scripts that are used to define the Structure of the SQL Instance, Import & Export Structure.

ii. Template Files that define the templates for the above Structure.

iii. Envernoment Files, which are used to define the variables

iv. Python Scripts to execute the above AIM using Deployment Manager

v. Here, Env File + Template File = YAML File

vi. This YAML files are used to create and update the Deployment Manager
