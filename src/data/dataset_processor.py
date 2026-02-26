import pandas as pd
from datasets import Dataset

class DatasetProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.raw_df = None
        self.dataset = None

    def load_data(self):
        self.raw_df = pd.read_csv(self.file_path)
        return self.raw_df

    def clean_data(self):
        self.raw_df = self.raw_df.dropna(subset=["Questions", "Answers"])
        return self.raw_df

    def format_instruction(self):
        formatted_data = []

        for _, row in self.raw_df.iterrows():
            prompt = (
                "<|system|>\n"
                "তুমি একজন সহানুভূতিশীল সহকারী।\n"
                "<|user|>\n"
                f"{row['Questions']}\n"
                "<|assistant|>\n"
                f"{row['Answers']}"
            )

            formatted_data.append({"text": prompt})

        self.dataset = Dataset.from_list(formatted_data)
        return self.dataset

    def train_val_split(self, test_size=0.1):
        return self.dataset.train_test_split(test_size=test_size)