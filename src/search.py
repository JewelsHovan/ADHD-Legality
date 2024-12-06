from tavily import TavilyClient
from config.config import TAVILY_API_KEY

class DrugSearcher:
    def __init__(self):
        self.client = TavilyClient(api_key=TAVILY_API_KEY)

    async def search_drug_availability(self, drug_name: str, country: str) -> dict:
        """
        Search for information about drug availability in a specific country
        """
        query = f"{drug_name} availability legal status prescription in {country}"
        
        try:
            search_result = self.client.search(
                query=query,
                search_depth="advanced",
                max_results=8
            )
            
            return {
                "drug": drug_name,
                "country": country,
                "results": search_result.get('results', [])
            }
        except Exception as e:
            print(f"Error searching for {drug_name} in {country}: {str(e)}")
            return None 