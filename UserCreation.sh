#!/bin/bash

# Path to CSV file containing user data
CSV_FILE="users.csv"

# Log in to Azure CLI (if not already logged in)
az login

# Set the Azure AD tenant ID
TENANT_ID="<your-tenant-id>"

# Loop through each row in the CSV file and create users
while IFS=, read -r DisplayName UserPrincipalName GivenName Surname Password; do
    # Create user in Azure AD
    az ad user create --display-name "$DisplayName" \
                      --user-principal-name "$UserPrincipalName" \
                      --given-name "$GivenName" \
                      --surname "$Surname" \
                      --password "$Password" \
                      --account-enabled true \
                      --force-change-password-next-login false \
                      --tenant-id "$TENANT_ID"
done < "$CSV_FILE"
