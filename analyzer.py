import pandas as pd
import matplotlib.pyplot as plt
import utils

class SalesAnalyzer:
    """Loading, cleaning and analyzing sales data."""

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.df = None

    def load_data(self):
        if not utils.file_exists(self.csv_path):
            raise FileExistsError(f'Die Datei {self.csv_path} existiert nicht')
        
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
        
        df["order_date"] = utils.parse_date(df["order_date"])
        
        df["order_amount"] = utils.parse_float(df["order_amount"])
        
        df["status"] = utils.normalize_status(df["status"])


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
    
    def order_status_distribution(self):
        return self.df["status"].value_counts(normalize=True) * 100

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
        plt.title("Monatlicher Umsatztrend")
        plt.xlabel("Monat")
        plt.ylabel("Umsatz")
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()


    def plot_order_amount_distribution(self, output_path):
        completed = self.df[self.df["status"] == "completed"]

        plt.figure()
        plt.hist(completed["order_amount"], bins=20)
        plt.title("Auftragsstatusverteilung")
        plt.xlabel("Bestellbetrag")
        plt.ylabel("Häufigkeit")
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()

    def generate_summary_report(self, output_path):
        lines = []

        lines.append("ZUSAMMENFASSENDER BERICHT ZUR VERTRIEBSANALYSE")
        lines.append("=" * 35)
        lines.append("")

        lines.append(f"Gesamtumsatz: {self.total_revenue():.2f}")
        lines.append(f"Durchschnittlicher Bestellwert: {self.average_order_value():.2f}")
        lines.append(f"Kundenzahl: {self.customer_count()}")
        lines.append("")

        lines.append("Umsatz nach Kategorien:")
        for category, revenue in self.revenue_by_category().items():
            lines.append(f"  {category}: {revenue:.2f}")

        lines.append("")
        lines.append("Auftragsstatusverteilung (%):")
        for status, pct in self.order_status_distribution().items():
            lines.append(f"  {status}: {pct:.1f}%")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    def export_top_customers(self, output_path, n=10):
        top = self.top_customers(n)
        top.to_csv(output_path, header=["total_spent"])

