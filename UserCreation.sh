#!/bin/bash

# Path to CSV file containing user data
CSV_FILE="users.csv"

# Set the Azure AD tenant ID
TENANT_ID="your-tenant-id"

# Loop through each row in the CSV file and create users
while IFS=, read -r DisplayName UserPrincipalName Password; do
    # Create user in Azure AD
    az ad user create --display-name "$DisplayName" \
                      --user-principal-name "$UserPrincipalName" \
                      --password "$Password" \
                      --force-change-password-next-sign-in true \

done < "$CSV_FILE"