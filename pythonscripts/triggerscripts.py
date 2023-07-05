
import os
import requests
import sys

TOKEN = str(sys.argv[0])
OWNER = str(sys.argv[1])
REPO = str(sys.argv[2])
Workflow_Name = str(sys.argv[3])
payload_Baseline_Number = str(sys.argv[4])
payload_Baseline_Revision = str(sys.argv[5])


print( "the toke value is")
def trigger_workflow(Workflow_Name,payload_Baseline_Number,payload_Baseline_Revision):

      headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {TOKEN}",
      }

      data = {
        "event_type": Workflow_Name,
        "client_payload": {
          'baselinetag': payload_Baseline_Number,
          'revision_number': payload_Baseline_Revision
        }
      }



trigger_workflow(Workflow_Name,payload_Baseline_Number,payload_Baseline_Revision)
