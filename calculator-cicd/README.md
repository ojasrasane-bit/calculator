# Calculator App with CI/CD

A simple Flask calculator deployed automatically with Jenkins, Docker and Minikube on AWS.

Made for the CCA 2 practical (Cloud Computing and DevOps).

## How it works

Push to GitHub -> Jenkins builds the Docker image -> runs tests -> pushes to Docker Hub -> deploys to Minikube.

## Files

- `app.py`, `calculator.py`, `templates/index.html` - the app
- `tests/test_app.py` - pytest tests
- `requirements.txt` - Flask, gunicorn, pytest
- `Dockerfile` - builds the image
- `Jenkinsfile` - the pipeline
- `k8s/` - Deployment and Service

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`. Run tests with `pytest`.

## Setup on the AWS server (Ubuntu EC2)

1. Install Docker, Jenkins, kubectl and Minikube.
2. Add the jenkins user to the docker group, then restart Jenkins:
   ```bash
   sudo usermod -aG docker jenkins
   sudo systemctl restart jenkins
   ```
3. Start Minikube and give Jenkins access to it (copy `~/.kube/config` and the minikube certs to `/var/lib/jenkins/.kube/`, then fix the paths inside the config).
4. In Jenkins add a credential: kind "Username with password", id `dockerhub-creds` (your Docker Hub login).
5. Edit `Jenkinsfile` and replace `YOUR_DOCKERHUB_USERNAME`.
6. Create a Pipeline job from this GitHub repo (Pipeline script from SCM) and add a GitHub webhook.
7. Open the app: `minikube service calculator-service --url`

## Demo: trigger a second run

1. Change something small in `templates/index.html` (for example the page title).
2. Commit and push.
3. Jenkins starts a new build. The footer shows the new build number after deploy.
