import asyncio
from src.search import DrugSearcher
from src.processor import DataProcessor
import pandas as pd
from config.config import ADHD_MEDICATIONS, TARGET_COUNTRIES

async def main():
    searcher = DrugSearcher()
    processor = DataProcessor()
    results = []

    for drug in ADHD_MEDICATIONS:
        for country in TARGET_COUNTRIES:
            # Search for information
            search_results = await searcher.search_drug_availability(drug, country)
            
            # Process and extract structured data
            if search_results:
                processed_data = await processor.extract_drug_info(search_results)
                if processed_data:
                    results.append(processed_data)
            
            # Be nice to APIs
            await asyncio.sleep(0.5)

    # Convert results to DataFrame
    df = pd.DataFrame(results)
    df.to_csv("adhd_drug_availability.csv", index=False)

if __name__ == "__main__":
    asyncio.run(main()) 