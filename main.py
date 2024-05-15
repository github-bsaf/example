import requests
import os
import sys

jenkins_url = 'https://jenkins-gldtn-tv2-sdk.cmo.conti.de'
job_name = 'pipeline_windows_CCIF'
build_parameters = {
   'JIRA_TICKETS': 'value1',
    # Add more parameters as needed
}

build_url = f'{jenkins_url}/job/{job_name}/buildWithParameters'
response = requests.post(build_url, auth=('uif91573', '1180779c578321dcb0b536279cfbe1530f'),data=build_parameters)
print(response.text)
