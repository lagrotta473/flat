# Definir o provedor (AWS)
provider "aws" {
  region = "us-east-1"  # Região da AWS
}

# Criar uma instância EC2 simples
resource "aws_instance" "my_instance" {
  ami           = "ami-0c55b159cbfafe1f0"  # AMI Ubuntu 20.04 LTS, você pode trocar pela AMI da sua escolha
  instance_type = "t2.micro"               # Tipo da instância (t2.micro é gratuito para novas contas)
  key_name      = "my-key"                 # Substitua pelo nome da sua chave SSH

  tags = {
    Name = "MyFirstInstance"
  }
}
