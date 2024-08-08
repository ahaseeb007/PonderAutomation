import datetime
import os

# Generate the current timestamp
current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
today_date = datetime.datetime.now().strftime("%Y_%m_%d")
report_filename = f"Report_{current_time}.html"

# Run pytest with the generated filename
os.system(f"pytest --html=reports/All_tests/{today_date}/{report_filename}")