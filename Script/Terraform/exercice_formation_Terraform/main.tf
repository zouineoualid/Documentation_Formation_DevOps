#Partie VPC 

resource "aws_vpc" "vpc_main" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "vpc_terraform_benoit"
  }
}

#Partie Gateway

resource "aws_internet_gateway" "gw_tp" {
  vpc_id = aws_vpc.vpc_main.id

  tags = {
    Name = "gateway_tp_terraform"
  }
}

#Partie Subnet

resource "aws_subnet" "subnet_private" {
  vpc_id     = aws_vpc.vpc_main.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "subnet_private_benoit"
  }
}

resource "aws_subnet" "subnet_public" {
  vpc_id     = aws_vpc.vpc_main.id
  cidr_block = "10.0.3.0/24"
  map_public_ip_on_launch = true
  tags = {
    Name = "subnet_public_benoit"
  }
}

#Partie route_table_private

resource "aws_route_table" "table_private" {
  vpc_id = aws_vpc.vpc_main.id

  route {
    cidr_block = "10.0.1.0/24"
    network_interface_id = aws_network_interface.network_database.id
  }

  tags = {
    Name = "route table private"
  }
}

#Partie route_table_public

resource "aws_route_table" "table_public" {
  vpc_id = aws_vpc.vpc_main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw_tp.id
  }

  tags = {
    Name = "route table public"
  }
}

#Create Network

resource "aws_network_interface" "network_web" {
  subnet_id       = aws_subnet.subnet_public.id
  security_groups = [aws_security_group.security_group_http.id]
}

resource "aws_network_interface" "network_database" {
  subnet_id       = aws_subnet.subnet_private.id
  security_groups = [aws_security_group.security_group_database.id]
}

#Partie EC2

resource "aws_instance" "web" {
  ami           = "ami-06e0ce9d3339cb039"
  instance_type = var.instance_type

  network_interface {
    network_interface_id = aws_network_interface.network_web.id
    device_index         = 0
  }

  tags = {
    Name = "terraform_web"
  }
}

resource "aws_instance" "database" {
  ami           = "ami-06e0ce9d3339cb039"
  instance_type = var.instance_type

  network_interface {
    network_interface_id = aws_network_interface.network_database.id
    device_index         = 0
  }

  tags = {
    Name = "terraform_database"
  }
}



resource "aws_security_group" "security_group_http" {
  name        = "allow_http"
  description = "Allow HTTP inbound traffic"
  vpc_id      = aws_vpc.vpc_main.id

  ingress {
    description      = "HTTP from VPC"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  ingress {
    description      = "SSH from VPC"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 65535
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "security_group_benoit_tp_80"
  }
}

resource "aws_security_group" "security_group_database" {
  name        = "allow_database"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.vpc_main.id

  ingress {
    description      = "database from VPC"
    from_port        = 3306
    to_port          = 3306
    protocol         = "tcp"
    cidr_blocks      = [aws_vpc.vpc_main.cidr_block]
  }

  ingress {
    description      = "SSH from VPC"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 65535
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "security_group_benoit_tp_1443"
  }
}


#partie OUTPUT
# output "ec2_instance_public_ip" {
#   description = "afficher adresse IP"
#   value = aws_instance.web.public_ip
  
# }

# output "ec2_instance_public_ip" {
#   description = "afficher adresse IP"
#   value = aws_instance.database.public_ip
  
# }