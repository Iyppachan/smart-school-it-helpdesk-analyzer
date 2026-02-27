import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def main():
    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data" / "raw" / "helpdesk_tickets.csv"
    figures_path = project_root / "reports" / "figures"

    print("Project root:", project_root)
    print("Data path:", data_path)
    print("Figures path:", figures_path)

    figures_path.mkdir(parents=True, exist_ok=True)
    print("Figures folder exists:", figures_path.exists())

    df = pd.read_csv(data_path)

    # Chart 1: Most Common Issues
    plt.figure()
    issue_counts = df["Issue_Type"].value_counts()
    sns.countplot(data=df, y="Issue_Type", order=issue_counts.index)
    plt.title("Most Common IT Issues in School")
    plt.xlabel("Number of Tickets")
    plt.ylabel("Issue Type")
    plt.tight_layout()
    plt.savefig(figures_path / "common_issues.png")
    print("Saved common_issues.png")
    plt.close()

    # Chart 2: Resolution Time by Priority
    plt.figure()
    sns.boxplot(data=df, x="Priority", y="Resolution_Time", order=["Low", "Medium", "High"])
    plt.title("Resolution Time by Priority")
    plt.xlabel("Priority")
    plt.ylabel("Resolution Time (minutes)")
    plt.tight_layout()
    plt.savefig(figures_path / "resolution_by_priority.png")
    print("Saved resolution_by_priority.png")
    plt.close()

    # Chart 3: Issues by Department Heatmap
    dept_issue = pd.crosstab(df["Department"], df["Issue_Type"])
    plt.figure(figsize=(10, 4))
    sns.heatmap(dept_issue, cmap="Blues")
    plt.title("Issues by Department")
    plt.tight_layout()
    plt.savefig(figures_path / "issues_by_department.png")
    print("Saved issues_by_department.png")
    plt.close()

    print("\nEDA finished.")


if __name__ == "__main__":
    main()