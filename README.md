# Scripts and notes used for GCP enumeration

[GCP pentesting guide (blog post)](https://slashparity.com/?p=938)

---
## Scripts 

**1. list_folders.py**  
**2. list_projects.py**  

These script accept as input a single folder ID or a file containing one folder ID per line.  
The result outputs the folders nested under the parent folder and the projects that are not under any folder.  

**3. project_assets_enum.py**  

Enumerates various assets within a GCP project, useful for understanding the environment you are in. Run it localy (requires gcloud) or in cloud compute instance, requires authentication & authorization. The output and results are based on the user’s permissions.
For more details, check out the [pentesting guide](https://slashparity.com/?p=938)


