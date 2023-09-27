# GitHub Data Migration

This project includes a collection of Python scripts designed to migrate repository data from GitHub Enterprise Server to GitHub Enterprise Cloud.

### Migrating Pull Requests

*pr_migrate* will first recreate all branches in the target repository. Once this is finished, it will then look through all **open** pull requests from the source repository and recreate them in the target repository, along with all of their commits. This will **not** create the target repository so that will have to be made before running this script.

### Migrating Issues

*issue_migrate* will grab all the issues listed in the source repository. It will then recreate them in the target repository utilizing GitHub's REST Api. Since we are recreating the issues to the new repository it will not retain the orginal issue number if there are pre-existing issues in the target repository. This script does not attach comments and fully re-assign the assigness to the issues should the account not exist in the target host. In place of that the script will attach the username in the description for future reference. 

>**Note:** Since we are recreating issues the creator the issue will be the user the PAT is associated with.

### Migrating Projects

*project_migrate* will utilize graphql to grab all projects from the source repository and recreate them in the target repository. This script will also not fully migrate project cards that are issues. In place of that it will create a card with the issue title as a placeholder once the issues are fully migrated over. This script is limited to classic project boards and does not have the ability to migrate project boards that are in beta.

## Prerequisites

### Access
  - Enterprise Server PAT
  - Enterprise Cloud PAT

>**Note:** Both PAT's require `repo` scope. These PAT's will need to be stored as repository secrets.

## Inputs

### pr_migrate
| Input            | Description                           | Required |
|------------------| --------------------------------------| ---------|
|base_ghes_hostname| Hostname for GHES instance            | true     |
|source_repo       | Source repository <org/repo> in GHES  | true     |
|target_repo       | Target repository <org/repo> in GHEC  | true     |
