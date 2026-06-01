wait paste this code in the readme too?

### 2. `lambda_function.py`
```python
import boto3
import json

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Extract Instance ID from the incoming security finding (e.g., GuardDuty or EventBridge)
    instance_id = event.get('detail', {}).get('resource', {}).get('instanceDetails', {}).get('instanceId')
    quarantine_sg_id = "sg-0abc123456isolated" # Pre-configured Isolated Security Group ID
    
    if not instance_id:
        print("[-] No valid Instance ID identified in the security event payload.")
        return {"status": "FAILED", "reason": "No Instance ID"}

    print(f"[!] Threat Detected: Initiating Quarantine Procedures for {instance_id}")

    try:
        # 1. Isolate the network interface by swapping the Security Group
        ec2.modify_instance_attribute(
            InstanceId=instance_id,
            Groups=[quarantine_sg_id]
        )
        print(f"[+] Successfully applied quarantine security group to {instance_id}")

        # 2. Tag the instance as compromised for forensic tracking
        ec2.create_tags(
            Resources=[instance_id],
            Tags=[
                {'Key': 'SecurityStatus', 'Value': 'QUARANTINED'},
                {'Key': 'IncidentIncidentID', 'Value': 'IR-2026-EVENT'}
            ]
        )
        
        return {
            "status": "SUCCESS",
            "isolatedInstance": instance_id,
            "appliedGroup": quarantine_sg_id
        }

    except Exception as e:
        print(f"[-] Incident response execution failure: {str(e)}")
        raise e
