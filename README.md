# DATA-ANALYTICS-PROJECT

This project transforms raw customer transaction data into a strategic Retention Playbook aimed at optimizing promotional spend and improving gross margins. By analyzing customer behavior across discount reliance, retention rates, and geographic brand strength, I identified segments where promotional discounts are hurting profitability rather than driving loyalty. The final deliverables include a dynamic Power BI dashboard, a comprehensive business recommendations report, and an executive presentation built in Gamma.

🎯 Objective: To define an Ideal Customer Profile (ICP), eliminate unprofitable promotional reliance, and propose a data-backed "Promotional Sunset" plan to increase gross margins by 8-12%.

Key Features: Customer demographics (age_group, customer_type), transaction history (Total Spend), product category, geographical data, and promotional flags used to engineer custom metrics like Discount Reliance Ratio (DRR) and Brand Pull Index.
🛠️ Tools & Technologies
Languages & Querying: Python (Pandas, NumPy, Seaborn), SQL (PostgreSQL / MySQL / SQL Server)
BI & Visualization: Power BI (DAX, Shape Maps, Scatter Plots)
Reporting & Presentation: Microsoft Word (Report), Gamma (Executive Deck)
📈 Steps & Methodology
Data Loading & Cleaning (Python): Imported raw data and handled missing values, duplicates, and data type conversions.
Feature Engineering (Python/SQL): Calculated advanced business metrics:
Discount Reliance Ratio (DRR): Share of revenue generated only under promotional conditions.
Brand Pull Index: Organic demand strength by location without discounts.
Entry Point % vs. Retention %: Category-level funnel analysis.
Database Integration (SQL): Loaded cleaned data into a relational database and wrote complex queries (CTEs, Window Functions) to segment customers by age, location, and DRR thresholds.
Dashboard Development (Power BI): Built an interactive dashboard tracking four core measurement pillars to visualize the intersection of discount reliance and customer value.
Strategic Reporting (Word): Authored the "Retention Playbook" detailing a step-by-step Promotional Sunset Plan, ICP definition, Risk Register, and Measurement Framework.
Executive Presentation (Gamma): Designed a high-impact, visually engaging slide deck summarizing the playbook for non-technical stakeholders.
📊 Dashboard & Deliverables
Dashboard Preview
<img width="1326" height="742" alt="Screenshot 2026-06-19 184301" src="https://github.com/user-attachments/assets/fa4a0710-a884-4d82-91a3-1c5ed65c8232" />


Dashboard Core Visuals:

Scatter Plot (DRR vs. ACV): Identifies age groups with high spend capacity but toxic promotional reliance.
Bar Chart (Entry Point vs. Retention): Highlights product categories attracting buyers but failing to retain them.
Shape Map (Brand Pull Index): Maps geographic markets to determine where discounts can be safely removed vs. where they are structurally necessary.
Funnel Chart: Visualizes customer types contributing disproportionate revenue.
