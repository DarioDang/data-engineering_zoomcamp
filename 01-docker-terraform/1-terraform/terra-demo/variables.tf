variable "credential" {
    description = "Path to the Google Cloud service account key file"
    default     = "./keys/my-creds.json"
}

variable "project" {
    description = "The Google Cloud project ID"
    default     = "isentropic-keep-461701-a7"
}

# Variables for Google Cloud project region using Terraform configuration
variable "region" {
    description = "The Google Cloud region for the resources"
    default     = "australia-southeast1"
}

# Variables for location project using Terraform configuration 
variable "location" {
    description = "The location for the resources"
    default     = "australia-southeast1"
}

#  Variables for Terraform configuration
variable "bigquery_dataset_name"{
    description = "Name of the BigQuery dataset"
    default     = "demo_dataset"
}

# Variables for Google Cloud provider configuration
variable "gcs_bucket_name" {
    description = "Name of the GCS bucket"
    default     = "demo-bucket-terraform-461701-a7"
}

# Variables for Google Cloud Storage bucket
variable "gcs_storage_class" {
    description = "Storage class for the GCS bucket"
    default     = "STANDARD"
}



