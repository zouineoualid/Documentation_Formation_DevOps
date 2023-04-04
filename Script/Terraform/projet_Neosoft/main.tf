#Initialisation VPC Noesoft - Francfort

resource "aws_vpc" "vpc_NeoSoft_Francfort" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "vpc_NeoSoft_Francfort"
  }
}

#Initialisation Gateway Neosoft - Francfort

resource "aws_internet_gateway" "Gateway_Neosoft_Francfort" {
  vpc_id = aws_vpc.vpc_NeoSoft_Francfort.id

  tags = {
    Name = "Gateway_Neosoft_Francfort"
  }
}

#Partie Subnet Public en 10.0.1 et en 10.0.2 - Neosoft - Francfort

resource "aws_subnet" "Subnet_Public_Neosoft_Francfort" {
  vpc_id     = aws_vpc.vpc_NeoSoft_Francfort.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone = "eu-central-1a"

  tags = {
    Name = "Subnet_Public_Neosoft_Francfort"
  }
}

resource "aws_subnet" "Subnet_Public_BiS_Neosoft_Francfort" {
  vpc_id     = aws_vpc.vpc_NeoSoft_Francfort.id
  cidr_block = "10.0.2.0/24"
  map_public_ip_on_launch = true
  availability_zone = "eu-central-1b"

  tags = {
    Name = "Subnet_Public_BiS_Neosoft_Francfort"
  }
}

#Partie Table de routage du Subnet Publique - Neosoft - Francfort
#
#On laisse le port 22 avec un cidr_block à 0.0.0.0/0 , mais l'idéal serait 
#de filtrer par l'adresse IP Publique de la société par soucis de sécurité

resource "aws_route_table" "Table_Public_Sub1_Neosoft_Francfort" {
  vpc_id = aws_vpc.vpc_NeoSoft_Francfort.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.Gateway_Neosoft_Francfort.id
  }

  tags = {
    Name = "table_public_Sub1_Neosoft_Francfort"
  }
}

#Attacher Table_Public_Sub1_Neosoft_Francfort à Subnet_Public_Neosoft_Francfort - NeoSoft - Francfort

resource "aws_route_table_association" "Association_Route_Table_Public" {
  subnet_id      = aws_subnet.Subnet_Public_Neosoft_Francfort.id
  route_table_id = aws_route_table.Table_Public_Sub1_Neosoft_Francfort.id
}

#Attacher Table_Public_Sub1_Neosoft_Francfort à Subnet_Public_BiS_Neosoft_Francfort - NeoSoft - Francfort

resource "aws_route_table_association" "Association_Route_Table_Public_BiS" {
  subnet_id      = aws_subnet.Subnet_Public_BiS_Neosoft_Francfort.id
  route_table_id = aws_route_table.Table_Public_Sub1_Neosoft_Francfort.id
}

#Partie Security_Group_Public - Neosoft - Francfort
#
#On laisse le port 22 avec un cidr_block à 0.0.0.0/0 , mais l'idéal serait 
#de filtrer par l'adresse IP Publique de la société par soucis de sécurité

resource "aws_security_group" "Security_Goup_Public_Neosoft_Francfort" {
  name        = "Security_Goup_Public_Neosoft_Francfort"
  description = "Security Group Public for Neosoft - Francfort"
  vpc_id      = aws_vpc.vpc_NeoSoft_Francfort.id

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
    Name = "Security_Goup_Public_Neosoft_Francfort"
  }
}


#Partie Security_Group_Public - Neosoft - Francfort
#
#On laisse le port 22 avec un cidr_block à 0.0.0.0/0 , mais l'idéal serait 
#de filtrer par l'adresse IP Publique de la société par soucis de sécurité

resource "aws_security_group" "Security_Goup_Public_BiS_Neosoft_Francfort" {
  name        = "Security_Goup_Public_BiS_Neosoft_Francfort"
  description = "Security Group Private for Neosoft - Francfort"
  vpc_id      = aws_vpc.vpc_NeoSoft_Francfort.id

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
    Name = "Security_Goup_Public_BiS_Neosoft_Francfort"
  }
}

#Create rules EKS Cluster - NeoSoft - Francfort

resource "aws_iam_role" "EKS_Cluster_IAM_Role_NeoSoft_Francfort" {
 name = "EKS_Cluster_IAM_Role_NeoSoft_Francfort"

 path = "/"

 assume_role_policy = <<EOF
{
 "Version" : "2012-10-17",
 "Statement" : [
  {
   "Effect" : "Allow",
   "Principal" : {
    "Service" : "eks.amazonaws.com"
   },
   "Action": "sts:AssumeRole"
  }
 ]
}
EOF

}

resource "aws_iam_role_policy_attachment" "AmazonEKSClusterPolicy" {
 policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
 role    = aws_iam_role.EKS_Cluster_IAM_Role_NeoSoft_Francfort.name
}

resource "aws_iam_role_policy_attachment" "AmazonEKSServicePolicy" {
 policy_arn = "arn:aws:iam::aws:policy/AmazonEKSServicePolicy"
 role    = aws_iam_role.EKS_Cluster_IAM_Role_NeoSoft_Francfort.name
}

resource "aws_iam_role_policy_attachment" "AmazonEKSVPCResourceController" {
 policy_arn = "arn:aws:iam::aws:policy/AmazonEKSVPCResourceController"
 role    = aws_iam_role.EKS_Cluster_IAM_Role_NeoSoft_Francfort.name
}

resource "aws_iam_role_policy_attachment" "eks-codebuild-sts-assume-role" {
 policy_arn = "arn:aws:iam::639962416620:policy/eks-codebuild-sts-assume-role"
 role    = aws_iam_role.EKS_Cluster_IAM_Role_NeoSoft_Francfort.name
}


##################################################################################################


#Initialisation EKS Cluster - NeoSoft - Francfort

resource "aws_eks_cluster" "EKS_NeoSoft_Francfort" {
  name     = "EKS_NeoSoft_Francfort"
  role_arn = aws_iam_role.EKS_Cluster_IAM_Role_NeoSoft_Francfort.arn

  vpc_config {
    subnet_ids = [aws_subnet.Subnet_Public_Neosoft_Francfort.id, aws_subnet.Subnet_Public_BiS_Neosoft_Francfort.id]
  } 

}

#Create rules EKS Cluster - NeoSoft - Francfort


resource "aws_iam_role" "EKS_Nodes_IAM_Role_NeoSoft_Francfort" {
  name = "EKS_Nodes_IAM_Role_NeoSoft_Francfort"

  assume_role_policy = jsonencode({
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
    Version = "2012-10-17"
  })
}

resource "aws_iam_role_policy_attachment" "AmazonEKSWorkerNodePolicy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
  role       = aws_iam_role.EKS_Nodes_IAM_Role_NeoSoft_Francfort.name
}

resource "aws_iam_role_policy_attachment" "AmazonEKS_CNI_Policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
  role       = aws_iam_role.EKS_Nodes_IAM_Role_NeoSoft_Francfort.name
}

resource "aws_iam_role_policy_attachment" "AmazonEC2ContainerRegistryReadOnly" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  role       = aws_iam_role.EKS_Nodes_IAM_Role_NeoSoft_Francfort.name
}

resource "aws_iam_role_policy_attachment" "EC2InstanceProfileForImageBuilderECRContainerBuilds" {
  policy_arn = "arn:aws:iam::aws:policy/EC2InstanceProfileForImageBuilderECRContainerBuilds"
  role       = aws_iam_role.EKS_Nodes_IAM_Role_NeoSoft_Francfort.name
}


#Initialisation EKS Nodes Public

resource "aws_eks_node_group" "EKS_NeoSoft_Node_Group_Public" {
  cluster_name    = aws_eks_cluster.EKS_NeoSoft_Francfort.name
  node_group_name = "EKS_NeoSoft_Node_Group_Public"
  node_role_arn   = aws_iam_role.EKS_Nodes_IAM_Role_NeoSoft_Francfort.arn
  subnet_ids      = [aws_subnet.Subnet_Public_Neosoft_Francfort.id, aws_subnet.Subnet_Public_BiS_Neosoft_Francfort.id]
  instance_types  = ["t2.micro"]

  scaling_config {
    desired_size = 1
    max_size     = 2
    min_size     = 1
  }

  update_config {
    max_unavailable = 1
  }

}

#Initilisation EKS Nodes Pivate

resource "aws_eks_node_group" "EKS_NeoSoft_Node_Group_Private" {
  cluster_name    = aws_eks_cluster.EKS_NeoSoft_Francfort.name
  node_group_name = "EKS_NeoSoft_Node_Group_Private"
  node_role_arn   = aws_iam_role.EKS_Nodes_IAM_Role_NeoSoft_Francfort.arn
  subnet_ids      = [aws_subnet.Subnet_Public_Neosoft_Francfort.id, aws_subnet.Subnet_Public_BiS_Neosoft_Francfort.id]
  instance_types  = ["t3.medium"]


  scaling_config {
    desired_size = 1
    max_size     = 2
    min_size     = 1
  }

  update_config {
    max_unavailable = 1
  }

}


##################################################################################################