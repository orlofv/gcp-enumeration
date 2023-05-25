
##Run this script on a GCP compute instance to enumerate any SAs that exist on the Instance.
##The results will vary depending on the account's permissions.

#!/bin/bash

# Define color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get a list of service account names
sa_list=$(curl -s -f -H "Metadata-Flavor: Google" "http://metadata/computeMetadata/v1/instance/service-accounts/")

# Loop through each service account and print its details
i=1
for sa in $sa_list; do
    echo -e "${GREEN}=== Service Account $i ===${NC}"
    echo "  Name: $sa"
    echo "  Email: "$(curl -s -f -H "Metadata-Flavor: Google" "http://metadata/computeMetadata/v1/instance/service>
    echo "  Aliases: "$(curl -s -f -H "Metadata-Flavor: Google" "http://metadata/computeMetadata/v1/instance/servi>
    echo "  Identity: "$(curl -s -f -H "Metadata-Flavor: Google" "http://metadata/computeMetadata/v1/instance/serv>
    echo "  Scopes: "$(curl -s -f -H "Metadata-Flavor: Google" "http://metadata/computeMetadata/v1/instance/servic>
    token=$(curl -s -f -H "Metadata-Flavor: Google" "http://metadata/computeMetadata/v1/instance/service-accounts/>
    access_token=$(echo "${token}" | jq -r .access_token)
    if [[ "${access_token}" != "" ]]; then
        echo -e "  Token: ${RED}${access_token}${NC}"
    fi
    echo ""
    ((i++))
done
