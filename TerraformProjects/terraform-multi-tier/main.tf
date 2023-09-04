terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.15.0"
    }
  }
}

# Create a VPC
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

# Create a Subnet
resource "aws_subnet" "main" {
  vpc_id                  = "${aws_vpc.main.id}"
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-west-1b"
}

# Create a Security Group
resource "aws_security_group" "allow_all" {
  name        = "allow_all"
  description = "Allow all inbound traffic"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 0
    to_port     = 65535
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

# Create a Web Server Instance
resource "aws_instance" "web" {
  ami                    = "ami-03f2f5212f24db70a"
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.main.id
  vpc_security_group_ids = [aws_security_group.allow_all.id]
  key_name               = "terraform-test"
  # ... other configurations ...
}

# Create an Application Server Instance
resource "aws_instance" "app" {
  ami                    = "ami-03f2f5212f24db70a"
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.main.id
  vpc_security_group_ids = [aws_security_group.allow_all.id]
  key_name               = "terraform-test"
  # ... other configurations ...
}

# Create a Database Server Instance
resource "aws_instance" "db" {
  ami                    = "ami-03f2f5212f24db70a"
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.main.id
  vpc_security_group_ids = [aws_security_group.allow_all.id]
  key_name               = "terraform-test"
  # ... other configurations ...
}

output "web_server_public_ip" {
  value = aws_instance.web.public_ip
}

output "app_server_public_ip" {
  value = aws_instance.app.public_ip
}

output "db_server_public_ip" {
  value = aws_instance.db.public_ip
}
