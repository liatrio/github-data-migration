# GitHub Data Migration

This project includes a collection of Python scripts designed to migrate repository data from GitHub Enterprise Server to GitHub Enterprise Cloud.

### Migrating Pull Requests

*pr_migrate* will first recreate all branches in the target repository. Once this is finished, it will then look through all **open** pull requests from the source repository and recreate them in the target repository, along with all of their commits. This will **not** create the target repository so that will have to be made before running this script.

### Migrating Issues

### Migrating Projects

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
