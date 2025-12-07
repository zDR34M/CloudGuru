variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-north-1"
}

variable "project_name" {
  description = "Project name prefix for tagging"
  type        = string
  default     = "cloudguru"
}

variable "my_ip_cidr" {
  description = "Your IP in CIDR format for bastion SSH"
  type        = string
  default     = "51.21.252.86/32"
}

variable "ssh_key_name" {
  description = "Existing EC2 key pair name for bastion host"
  type        = string
  default     = "trtech"
}

variable "backend_image" {
  description = "ECR image URI (including tag) for backend"
  type        = string
  default     = "065727387548.dkr.ecr.eu-north-1.amazonaws.com/cloudguru-backend:latest"
}
