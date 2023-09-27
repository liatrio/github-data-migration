# GitHub Data Migration

This project includes a collection of Python scripts designed to migrate data to GitHub Enterprise Cloud.

## Using workflow

### Prerequisites

Secrets needed:
  - Enterprise Server personal access token
  - Enterprise Cloud personal access token

Scopes for PATs are `repo` because the scope of this project is to migrate repositories and their data.

Inputs required for manual trigger:
  - Enterprise Server host URL 
  - source respository format: `owner/repository` 
  - destination repository format: `owner/repository`
