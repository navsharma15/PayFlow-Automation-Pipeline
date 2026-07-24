import subprocess
import logging


# -----------------------------
# Logging Configuration
# -----------------------------

logging.basicConfig(
    filename="../logging/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


# -----------------------------
# Automation Pipeline
# -----------------------------

logging.info("========== Automation Started ==========")

print("Automation Started")


try:

    # Step 1: Generate Data
    subprocess.run(
        ["python", "02_generate_daily_data.py"],
        check=True
    )

    logging.info("Data Generation Completed")
    print("Data Generation Completed")


    # Step 2: Append Data
    subprocess.run(
        ["python", "03_append_data.py"],
        check=True
    )

    logging.info("Data Append Completed")
    print("Data Append Completed")


    # Step 3: Clean Data
    subprocess.run(
        ["python", "04_clean_data.py"],
        check=True
    )

    logging.info("Data Cleaning Completed")
    print("Data Cleaning Completed")


    # Step 4: Load SQL
    subprocess.run(
        ["python", "05_load_sql.py"],
        check=True
    )

    logging.info("SQL Loading Completed")
    print("SQL Loading Completed")


    # Success

    logging.info("Automation Completed Successfully")
    logging.info("======================================")


    print("Automation Completed Successfully")


except Exception as e:

    logging.error(f"Automation Failed: {e}")

    print("Automation Failed")
    print(e)