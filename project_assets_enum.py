#!/usr/bin/env python3

import os

# Color variables
green = '\033[0;32m'
nocolor = '\033[0m'

# Initialization
os.system('gcloud init')
print()

# Output Directory
directory = input("Please enter Output Directory Name : ")
os.makedirs(directory, exist_ok=True)
os.makedirs(f"{directory}/networking", exist_ok=True)
print()

# Org / Folders
with open(f"{directory}/organization.txt", "w") as f:
    os.system("gcloud organizations list > temp.txt")
    f.write(open("temp.txt").read())
    os.remove("temp.txt")
    f.write("\n")
    org = os.popen("gcloud organizations list | sed -n 2p | awk '{print $2}'").read().strip()
    os.system(f"gcloud resource-manager folders list --organization={org} >> {directory}/organization.txt")

# Clusters - GKE
os.system(f"gcloud container clusters list > {directory}/clusters.txt")
print(f"{green}Found GKE clusters, check {directory}/clusters.txt for additional information {nocolor}")
print()

# Compute IPs
os.system(f"gcloud --format='value(networkInterfaces[0].accessConfigs[0].natIP)' compute instances list | uniq | grep '\\S' > {directory}/networking/public_ips.txt")
os.system(f"gcloud compute instances list | awk '{{print $5}}' | grep ^1 | uniq > {directory}/networking/private_ips.txt")
pubips = len(open(f"{directory}/networking/public_ips.txt").readlines())
privips = len(open(f"{directory}/networking/private_ips.txt").readlines())
print(f"{green}{pubips} Public IPs {nocolor}")
print(f"{green}{privips} Private IPs {nocolor}")

# Buckets
os.system(f"gcloud storage ls | cut -f3 -d '/' > {directory}/buckets.txt")
buckets = len(open(f"{directory}/buckets.txt").readlines())
print(f"{green}{buckets} Storage Buckets {nocolor}")

# Compute
os.system(f"gcloud compute instances list > {directory}/compute_instances.txt")
ci = len(open(f"{directory}/compute_instances.txt").readlines())
print(f"{green}{ci} Compute Instances {nocolor}")

# Networks
os.system(f"gcloud compute networks subnets list > {directory}/networking/subnets.txt")
subnets = len(open(f"{directory}/networking/subnets.txt").readlines())
print(f"{green}{subnets} Subnets {nocolor}")

# Firewall
# os.system(f"gcloud compute firewall-rules list > {directory}/firewalls.txt")
# firewalls = len(open(f"{directory}/firewalls.txt").readlines())
# print(f"{green}{firewalls} Firewall Rules {nocolor}")

# IAM (user's permissions)
project = os.popen("gcloud config get-value project").read().strip()
os.system(f"gcloud projects get-iam-policy {project} > {directory}/iam.txt")

# Functions
os.system(f"gcloud functions list > {directory}/functions.txt")
functions = len(open(f"{directory}/functions.txt").readlines())
print(f"{green}{functions} Cloud Functions {nocolor}")

# PubSub
os.system(f"gcloud pubsub subscriptions list > {directory}/pubsub.txt")
print(f"{green}Found pubsub subscriptions, please check {directory}/pubsub.txt for additional information. {nocolor}")

# Peering Networks
os.system(f"gcloud compute networks peerings list > {directory}/networking/peering.txt")
with open(f"{directory}/networking/peering.txt", "r") as f:
    peering = len(f.readlines())
peer = peering - 1
print(f"{green}{project} is interconnected (peered) to {peer} networks {nocolor}")
print("")

print(f"{green}Results saved under {directory} directory. Exiting! {nocolor}")

