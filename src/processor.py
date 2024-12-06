from langchain_openai import ChatOpenAI
from config.config import OPENROUTER_API_KEY

class DataProcessor:
    def __init__(self):
        self.client = ChatOpenAI(
            model="google/gemini-flash-1.5-8b",
            openai_api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",

        )

    async def extract_drug_info(self, search_results: dict) -> dict:
        """
        Process search results using LLM to extract structured information
        """
        if not search_results:
            return None

        # Use 'content' field instead of 'text'
        context = "\n".join([result.get('content', '') for result in search_results["results"]])

        print("Context:", context)
        
        prompt = f"""
        Based on the following information about {search_results['drug']} in {search_results['country']}, 
        please extract and provide the following details in a structured format:
        1. Legal Status (legal/illegal/prescription-only)
        2. Availability (easily available/restricted/not available)
        3. Prescription Requirements
        4. Any specific regulations or restrictions
        
        Context:
        {context}
        """

        try:
            response = await self.client.ainvoke(prompt)
            
            return {
                "drug": search_results["drug"],
                "country": search_results["country"],
                "analysis": response.content
            }
        except Exception as e:
            print(f"Error processing results: {str(e)}")
            return None 