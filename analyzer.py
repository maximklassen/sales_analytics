import pandas as pd
import matplotlib.pyplot as plt

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

    def total_revenue(self):
        """Umsatz"""
        return self.df.loc[
            self.df["status"] == "completed", "order_amount"
        ].sum()

    def average_order_value(self):
        completed = self.df[self.df["status"] == "completed"]
        return completed["order_amount"].mean()

    def average_order_value(self):
        completed = self.df[self.df["status"] == "completed"]
        return completed["order_amount"].mean()

    def customer_count(self):
        return self.df["customer_id"].nunique()

    def revenue_by_category(self):
        return (
            self.df[self.df["status"] == "completed"].groupby("product_category")["order_amount"].sum().sort_values(ascending=False)
        )

    def top_customers(self, n=10):
        return (
            self.df[self.df["status"] == "completed"].groupby("customer_id")["order_amount"].sum().sort_values(ascending=False).head(n)
        )

    def repeat_customer_rate(self):
        orders_per_customer = self.df.groupby("customer_id").size()
        repeat_customers = orders_per_customer[orders_per_customer > 1]
        return len(repeat_customers) / len(orders_per_customer)

    def monthly_revenue(self):
        completed = self.df[self.df["status"] == "completed"]
        # completed["month"] = completed["order_date"].dt.to_period("M")
        # completed.groupby("month")["order_amount"].sum()
        return (
            completed.set_index("order_date").resample("ME")["order_amount"].sum()
        )
    

    """ Charts """
    
    def plot_revenue_by_category(self, output_path):
        data = self.revenue_by_category()

        plt.figure()
        data.plot(kind="bar")
        plt.title("Umsatz nach Kategorien")
        plt.xlabel("Kategorie")
        plt.ylabel("Umsatz")
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()

    def plot_monthly_revenue(self, output_path):
        data = self.monthly_revenue()

        plt.figure()
        data.plot()
        plt.title("Monthly Revenue Trend")
        plt.xlabel("Month")
        plt.ylabel("Revenue")
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()


    def plot_order_amount_distribution(self, output_path):
        completed = self.df[self.df["status"] == "completed"]

        plt.figure()
        plt.hist(completed["order_amount"], bins=20)
        plt.title("Order Amount Distribution")
        plt.xlabel("Order Amount")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
