variable "aws_region" {
  default = "ap-south-1"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "Your existing AWS EC2 key pair name"
}

variable "docker_image" {
  description = "Your DockerHub image name"
}
