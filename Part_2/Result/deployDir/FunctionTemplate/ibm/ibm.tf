# Access variable from terraform.tfvars
variable "ibmcloud_api_key" {}

# Support ibm provider
terraform {
  required_providers {
    ibm = {
      source  = "IBM-Cloud/ibm"
      version = "~> 1.25.0"
    }
  }
}

variable "region" {
  type        = string
  description = "The AWS region for the deployment. See https://cloud.ibm.com/docs/containers?topic=containers-regions-and-zones"
  default = "eu-de"
}

# Credentials and region configuration
provider "ibm" {
  ibmcloud_api_key   = var.ibmcloud_api_key
  region             = var.region
  alias              = "region"
}


locals {
  node_functions = ["template-node"]
  function_docker_names = ["template-python"]
  function_docker_images = ["ibmfunctions/action-python-v3.7"]
}



# Function configuration
resource "ibm_function_action" "functions" {
  count = length(local.node_functions)

  name      = local.node_functions[count.index]
  namespace = "apollo"
  provider = ibm.region

  exec {
    kind = "nodejs:12"
    code_path = "tmp/${local.node_functions[count.index]}.zip"
  }

  # Timeout and memory
  limits {
    timeout = "60000"
    memory  = "128"
  }

  user_defined_annotations = <<EOF
        [
    {
        "key":"web-export",
        "value":true
    }
]
EOF


}

resource "ibm_function_action" "functions_docker" {
  count = length(local.function_docker_names)

  name      = local.function_docker_names[count.index]
  namespace = "apollo"
  provider = ibm.region

  exec {
    kind   = "blackbox"    
    image  = "${local.function_docker_images[count.index]}"
    code_path = "tmp/${local.function_docker_names[count.index]}.zip"
  }

  # Timeout and memory
  limits {
    timeout = "60000"
    memory  = "128"
  }

  user_defined_annotations = <<EOF
        [
    {
        "key":"web-export",
        "value":true
    }
]
EOF

}



output "url_template-node" {
  value = "${ibm_function_action.functions[0].target_endpoint_url}.json"
}

output "url_template-python" {
  value = "${ibm_function_action.functions_docker[0].target_endpoint_url}.json"
}