# 🚀 CloudGuru DevOps Project

This project demonstrates a **complete production-grade DevOps pipeline** using modern cloud-native technologies:

- ✅ Python Flask Backend
- ✅ Docker & Amazon ECR
- ✅ Terraform Infrastructure as Code
- ✅ Amazon ECS Fargate
- ✅ Application Load Balancer (ALB)
- ✅ GitHub Actions CI/CD
- ✅ Manual Infrastructure Destroy Pipeline

---

## 🧱 Architecture Overview

    Developer Push → GitHub Actions → Docker Build → Amazon ECR
    ↓
    Terraform Infrastructure
    ↓
    ECS Fargate → ALB → Internet


---

## 📁 Project Structure

    CloudGuru/
    ├── app/
    │ └── backend/
    │ ├── app/
    │ ├── Dockerfile
    │ ├── requirements.txt
    │ └── docker-compose.yml
    ├── terraform/
    │ ├── main.tf
    │ ├── variables.tf
    │ ├── outputs.tf
    │ ├── providers.tf
    │ └── backend.tf
    └── .github/
    └── workflows/
    ├── deploy.yml
    └── terraform-destroy.yml


---

## 🐍 Backend API

### ✅ Health Check Endpoint

GET /health


### ✅ Example Response

```json
{
  "status": "ok",
  "service": "backend-service",
  "environment": "prod"
}
```

---

## 🐳 Docker Usage
### Build Image Locally

```bash
cd app/backend
docker build -t backend-service .
```
Run Locally

docker-compose up
```bash
docker-compose up
```
 ---
## ☁️ AWS Infrastructure (Terraform)
### ✅ Resources Created

    VPC

    Public & Private Subnets

    Internet Gateway

    NAT Gateway

    Application Load Balancer

    ECS Cluster (Fargate)

    ECS Service & Task Definition

    CloudWatch Logs

    Security Groups

## ✅ Terraform Apply
```bash
cd terraform

terraform init

terraform apply \
  -var="my_ip_cidr=YOUR_IP/32" \
  -var="ssh_key_name=YOUR_KEYPAIR" \
  -var="backend_image=YOUR_ECR_IMAGE"
```
## ✅ Terraform Destroy (Local)
```bash
terraform destroy \
  -var="my_ip_cidr=YOUR_IP/32" \
  -var="ssh_key_name=YOUR_KEYPAIR" \
  -var="backend_image=YOUR_ECR_IMAGE"
```
---

## 🔁 CI/CD with GitHub Actions
### ✅ Deployment Pipeline

Triggered automatically on every push to main:

    Build Docker image

    Push image to Amazon ECR

    Force redeployment on Amazon ECS

    ✅ Required GitHub Secrets
    Secret Name	Description
    AWS_ACCESS_KEY_ID	IAM access key
    AWS_SECRET_ACCESS_KEY	IAM secret key
    AWS_ACCOUNT_ID	AWS account ID
    💣 One-Click Terraform Destroy from GitHub

### A manual GitHub Actions workflow allows the infrastructure to be destroyed safely:

    GitHub → Actions → Terraform Destroy → Run Workflow

This deletes:

    ECS Cluster & Services

    ALB & Target Groups

    VPC & Networking

    Security Groups

    All Terraform-managed infrastructure

---

## ✅ Live Health Check Test

```bash
curl http://<ALB_DNS_NAME>/health
```

### Expected Response:
```json
{
  "status": "ok"
}
```
---
## 🧠 What This Project Demonstrates

- ✅ End-to-end DevOps automation
- ✅ Infrastructure as Code (Terraform)
- ✅ Containerized microservice deployment
- ✅ Secure AWS networking
- ✅ CI/CD automation with GitHub Actions
- ✅ Zero-downtime deployments
- ✅ Full lifecycle infrastructure management
- ✅ Project Status

```
✔ Fully functional
✔ CI/CD enabled
✔ Cloud infrastructure automated
✔ Production-ready architecture
```
