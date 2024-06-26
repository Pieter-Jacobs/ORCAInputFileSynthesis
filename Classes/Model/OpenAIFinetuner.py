import os
import requests
from openai import OpenAI
import csv


class OpenAIFinetuner:
    """Simple wrapper class that facilitates the use of the OpenAI SDK"""

    def __init__(self):
        self.client = OpenAI()

    def upload_dataset(self, dataset_path):
        """Uploads a dataset so that it can be used for finetuning"""
        path = dataset_path
        file_object = self.client.files.create(
            file=open(path, "rb"),
            purpose="fine-tune"
        )
        return file_object.id

    def start_finetuning_job_parameterized(self, model, train_file, val_file, suffix, n_epochs, batch_size, learning_rate_multiplier):
        """Creates a finetuning job with provided parameters"""

        self.client.fine_tuning.jobs.create(
            training_file=train_file,
            validation_file=val_file,
            model=model,
            suffix=suffix,
            hyperparameters={
                "n_epochs": n_epochs,
                "batch_size": batch_size,
                "learning_rate_multiplier": learning_rate_multiplier
            }
        )

    def start_finetuning_job(self, model, train_file, val_file, suffix):
        """Creates a finetuning job where OpenAI provides the parameters"""

        self.client.fine_tuning.jobs.create(
            training_file=train_file,
            validation_file=val_file,
            model=model,
            suffix=suffix
        )

    def save_finetuning_job_results_to_csv(self, csv_filename):
        """Checks the most recent succesful finetuning job, and saves the results from it to csv"""
        def save_to_csv(content, filename):
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['content'])  # Write header
                writer.writerow([content])

        headers = {
            'Authorization': f"Bearer {os.environ['OPENAI_API_KEY']}"
        }

        last_job = self.client.fine_tuning.jobs.list(limit=1)
        result_files = last_job.data[0].result_files
        for result_file in result_files:
            response = requests.get(
                f"https://api.openai.com/v1/files/{result_file}/content", headers=headers)

            # Check if request was successful (status code 200)
            if response.status_code == 200:
                content = response.text  # Get content from response
                save_to_csv(content, csv_filename)
            else:
                print(
                    f"Failed to retrieve content from {result_file}. Status code: {response.status_code}")
