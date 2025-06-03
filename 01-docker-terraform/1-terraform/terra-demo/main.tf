# This Terraform configuration file creates a Google Cloud Storage bucket and a BigQuery dataset.
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.37.0"
    }
  }
}

# Configure the Google Cloud provider
provider "google" {
  # Configuration options
  credentials = file(var.credential)
  project     = var.project
  region      = var.region
}

# Create a Google Compute Engine instance
resource "google_storage_bucket" "demo-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

# Create a BigQuery dataset
resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = var.bigquery_dataset_name
  location = var.location
}