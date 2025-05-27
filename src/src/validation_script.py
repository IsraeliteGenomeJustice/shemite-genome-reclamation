import pandas as pd

# Load the CSV file
df = pd.read_csv('data/suppression_evidence.csv')

# Expected SNPs
expected_snps = {'CTS6773', 'M3987', 'Y471213', 'SNP4', 'SNP5', 'SNP6', 'SNP7', 'SNP8', 'SNP9'}

# Validate the SNPs in the CSV
actual_snps = set(df['SNP'])
missing_snps = expected_snps - actual_snps

# Print validation results
if missing_snps:
    print(f"Validation failed: Missing SNPs: {missing_snps}")
    exit(1)
else:
    print(f"Validation successful: All {len(expected_snps)} SNPs found.")
    print(f"Summary: {len(df)} suppressed SNPs detected in {df['Sample'].nunique()} samples.")
  Add src/validation_script.py to validate suppression evidence
