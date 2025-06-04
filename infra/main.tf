provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "ml_api" {
  ami           = "ami-08e5424edfe926b43" # Amazon Linux 2 (ap-south-1)
  instance_type = var.instance_type
  key_name      = var.key_name

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              amazon-linux-extras install docker -y
              service docker start
              usermod -a -G docker ec2-user
              docker run -d -p 5000:5000 ${var.docker_image}
              EOF

  tags = {
    Name = "ML-API-Server"
  }
}

resource "aws_security_group" "ml_api_sg" {
  name        = "ml-api-sg"
  description = "Allow 5000 and SSH"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_network_interface_sg_attachment" "sg_attachment" {
  security_group_id    = aws_security_group.ml_api_sg.id
  network_interface_id = aws_instance.ml_api.primary_network_interface_id
}
