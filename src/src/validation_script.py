import pandas as pd
import sys

try:
    print("Loading data/suppression_evidence.csv...")
    df = pd.read_csv('data/suppression_evidence.csv')
    print("CSV Contents:")
    print(df.to_string())

    expected_columns = {'SNP', 'Sample', 'Status'}
    actual_columns = set(df.columns)
    if not expected_columns.issubset(actual_columns):
        print(f"Validation failed: Missing columns {expected_columns - actual_columns}")
        sys.exit(1)

    expected_snps = {'CTS6773', 'M3987', 'Y471213', 'SNP4', 'SNP5', 'SNP6', 'SNP7', 'SNP8', 'SNP9'}
    actual_snps = set(df['SNP'])
    missing_snps = expected_snps - actual_snps

    if missing_snps:
        print(f"Validation failed: Missing SNPs: {missing_snps}")
        sys.exit(1)
    else:
        print(f"Validation successful: All {len(expected_snps)} SNPs found.")
        print(f"Summary: {len(df)} suppressed SNPs detected in {df['Sample'].nunique()} samples.")
except Exception as e:
    print(f"Validation script error: {str(e)}")
    sys.exit(1)
    Add src/validation_script.py with improved logging and error handling
