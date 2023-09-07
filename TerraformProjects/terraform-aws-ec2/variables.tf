variable "aws_region" {
  description = "The AWS region to create resources in."
  default     = "us-west-2"
}

variable "instance_type" {
  description = "The type of instance to create."
  default     = "t2.micro"
}

variable "ami" {
  description = "The AMI to use for the instance."
  default     = "ami-0c94855ba95c71c99" # Amazon Linux 2 LTS AMI
}
