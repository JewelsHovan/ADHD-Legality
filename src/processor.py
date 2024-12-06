from langchain_openai import ChatOpenAI
from config.config import OPENROUTER_API_KEY, MODEL
from .models import DrugInfo

class DataProcessor:
    def __init__(self):
        self.client = ChatOpenAI(
            model=MODEL,
            openai_api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )
        # Create a structured output model
        self.structured_model = self.client.with_structured_output(DrugInfo)

    async def extract_drug_info(self, search_results: dict) -> dict:
        """
        Process search results using LLM to extract structured information
        """
        if not search_results:
            return None

        context = "\n".join([result.get('content', '') for result in search_results["results"]])
        
        prompt = f"""
        Based on the following information about {search_results['drug']} in {search_results['country']}, 
        extract the drug's legal and regulatory information.
        
        Context:
        {context}
        """

        try:
            # Get structured response
            drug_info = await self.structured_model.ainvoke(prompt)
            
            return {
                "drug": search_results["drug"],
                "country": search_results["country"],
                "analysis": drug_info.model_dump()
            }
        except Exception as e:
            print(f"Error processing results: {str(e)}")
            return None 