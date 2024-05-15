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
response = requests.get("https://github.com", auth=('safibechir@yahoo.fr', 'bsaf_2016'))
print(response.text)
