from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load

def main():
    # 1. Extract data
    df = extract()
    print(f"✅ Extracted {len(df)} rows")

    # 2. Transform data
    df = transform(df)
    print(f"✅ Transformed: {df.shape}")

    # 3. Load into Postgres
    load(df)
    print("✅ Data successfully loaded into Postgres")

if __name__ == "__main__":
    main()
