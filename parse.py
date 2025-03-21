from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from typing import List

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="mistral:7b")

def parse_with_ollama(dom_chunks: List[str], parse_description: str) -> List[str]:
    prompt = ChatPromptTemplate.from_template(template)
    # Chain the prompt with the LLM model
    chain = prompt | model

    parsed_results = []


    # Process each DOM chunk through the LLM
    for i, chunk in enumerate(dom_chunks):
        print(f"Parsed batch {i+1} of {len(dom_chunks)}")
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})
        parsed_results.append(response)

    return "\n".join(parsed_results)


