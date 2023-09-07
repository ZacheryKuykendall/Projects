variable "client_id" {
  description = "The client ID for AKS service principal"
}

variable "client_secret" {
  description = "The secret for AKS service principal"
}

variable "agent_count" {
  description = "The number of agents (VMs) in the AKS cluster"
  default     = 1
}
