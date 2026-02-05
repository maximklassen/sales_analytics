import pandas as pd


class SalesAnalyzer:
    """Loading, cleaning and analyzing sales data."""

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.csv_path)
        return self.df
    
    def inspect_data(self):
        return {
            "info": self.df.info(),
            "describe": self.df.describe(include="all")
        }

    def clean_data(self):
        df = self.df.copy()
        df.drop_duplicates(inplace=True)
        
        df["order_date"] = pd.to_datetime(
            df["order_date"], errors="coerce"
        )
        
        df["order_amount"] = pd.to_numeric(
            df["order_amount"], errors="coerce"
        )
        
        df["status"] = df["status"].fillna("completed")

        df = df.dropna(subset=["order_date", "order_amount"])

        self.df = df
        return df
    
    def export_clean_data(self, output_path: str):
        self.df.to_csv(output_path, index=False)

