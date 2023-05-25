# Scripts and notes used for GCP enumeration

[GCP pentesting guide (blog post)](https://slashparity.com/?p=938)

---
## Scripts 

**1. sa_enum.py**  

Run this script on a GCP compute instance to enumerate any SAs that exist on the Instance.  
The results will vary depending on the account's permissions.  

**2. list_folders.py**  
**3. list_projects.py**  

The scripts accept as input a single folder ID or a file containing one folder ID per line.  
The result outputs the folders nested under the parent folder and the projects that are not under any folder.  

**3. project_assets_enum.py**  

Enumerates various assets within a GCP project, useful for understanding the environment you are in. Run it localy (requires gcloud) or in cloud compute instance, requires authentication & authorization. The output and results are based on the user’s permissions.
For more details, check out the [pentesting guide](https://slashparity.com/?p=938#Enumeration_Script)  

---  

## 3rd Party Tools  

**1. [GCP Token Reuse](https://github.com/RedTeamOperations/GCPTokenReuse)**  

The script checks if an access token is active or expired. If the token is valid it creates a gcloud configuration based on that token.  

_Syntax_ : 
 
 `python3 Gcp-Token-Updater.py -I --access-token <access_token> --account-name <the gcloud config/account name you want to assign>`  

<img width="807" alt="2023-05-25_10-51" src="https://github.com/slashparity/gcp-enumeration/assets/80419690/5158cfe7-6d7a-491a-9c0d-9ba31168e401">
