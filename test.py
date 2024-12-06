import asyncio
from src.search import DrugSearcher

async def test_search():
    searcher = DrugSearcher()
    result = await searcher.search_drug_availability("Adderall", "United States")
    print("Search Results:", result)
    # Print the structure to understand what we're getting back
    if result and 'results' in result:
        print("\nFirst result structure:")
        print(result['results'][0] if result['results'] else "No results found")

if __name__ == "__main__":
    asyncio.run(test_search())
