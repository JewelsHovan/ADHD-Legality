import asyncio
from src.search import DrugSearcher
from src.processor import DataProcessor
import pandas as pd
from config.config import ADHD_MEDICATIONS, TARGET_COUNTRIES

async def main():
    print("Starting drug availability search...")
    searcher = DrugSearcher()
    processor = DataProcessor()
    results = []

    total_drugs = len(ADHD_MEDICATIONS)
    total_countries = len(TARGET_COUNTRIES)
    current = 0
    total = total_drugs * total_countries

    for drug in ADHD_MEDICATIONS:
        for country in TARGET_COUNTRIES:
            current += 1
            print(f"\nProcessing {drug} for {country} ({current}/{total})...")
            
            # Search for information
            print("Searching for drug information...")
            search_results = await searcher.search_drug_availability(drug, country)
            
            # Process and extract structured data
            if search_results:
                print("Processing search results...")
                processed_data = await processor.extract_drug_info(search_results)
                if processed_data:
                    print("Successfully extracted drug information")
                    results.append(processed_data)
                else:
                    print("Failed to process search results")
            else:
                print("No search results found")
            
            # Be nice to APIs
            await asyncio.sleep(0.5)

    print("\nConverting results to CSV...")
    # Convert results to DataFrame
    df = pd.DataFrame(results)

    print("\nProcessing and transforming data...")
    try:
        # Convert string representation of dictionary to actual dictionaries
        df['analysis'] = df['analysis'].apply(eval)

        # Split the analysis column into separate columns
        analysis_fields = ['legal_status', 'availability', 'prescription_requirements', 'regulations']
        for field in analysis_fields:
            df[field] = df['analysis'].apply(lambda x: x.get(field, ''))  # Using get() with default value

        # Drop the original analysis column
        df = df.drop('analysis', axis=1)
        
        print("Data transformation successful")
    except Exception as e:
        print(f"Error during data transformation: {e}")
        print("Saving original dataframe without transformations")

    print("Saving results to CSV...")
    df.to_csv("adhd_drug_availability.csv", index=False)
    print("Done! Results saved to adhd_drug_availability.csv")

if __name__ == "__main__":
    asyncio.run(main())