# prod-cicd-demo-app

This is the application repository.

It contains::

- Flask application
- Dockerfile
- GitHub Actions workflow

The pipeline builds an immutable image using commit SHA, pushes it to ECR, then updates the GitOps repository.

Required GitHub repository secrets:

```text
AWS_ROLE_ARN
CONFIG_REPO_TOKEN
```

Required GitHub repository variables:

```text
AWS_REGION
ECR_REPOSITORY
CONFIG_REPO
CONFIG_PATH
```
