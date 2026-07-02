import os
from dotenv import load_dotenv
from openai import OpenAI  # <-- We are now using the standard client

# The 'override=True' forces Python to use the exact values in your .env
load_dotenv(override=True)

def test_azure_connections():
    print("=== Starting Azure OpenAI Diagnostic Test (v1 API Architecture) ===")
    
    # ---------------------------------------------------------
    # Test 1: The Mini Model (Router)
    # ---------------------------------------------------------
    print("\n--- Testing 'Mini' Deployment ---")
    
    # We construct the exact v1 URL path the new Azure architecture requires
    base_endpoint = os.getenv("AZURE_MINI_ENDPOINT").rstrip('/')
    v1_base_url = f"{base_endpoint}/openai/v1/"
    mini_deployment = os.getenv("AZURE_MINI_DEPLOYMENT")
    
    print(f"Targeting v1 Base URL: {v1_base_url}")
    print(f"Targeting Deployment:  {mini_deployment}")
    
    try:
        # Note: We instantiate OpenAI(), NOT AzureOpenAI()
        client_mini = OpenAI(
            api_key=os.getenv("AZURE_MINI_API_KEY"),
            base_url=v1_base_url
        )
        
        response_mini = client_mini.chat.completions.create(
            model=mini_deployment,
            messages=[{"role": "user", "content": "Say: 'Mini router connection successful!'"}]
        )
        print(f"✅ SUCCESS: {response_mini.choices[0].message.content}")
        
    except Exception as e:
        print(f"❌ FAILED. Error details:\n{e}")

    # ---------------------------------------------------------
    # Test 2: The Main Model (Mentor Voice)
    # ---------------------------------------------------------
    print("\n--- Testing 'Main' Deployment ---")
    
    base_endpoint_main = os.getenv("AZURE_MAIN_ENDPOINT").rstrip('/')
    v1_base_url_main = f"{base_endpoint_main}/openai/v1/"
    main_deployment = os.getenv("AZURE_MAIN_DEPLOYMENT")
    
    print(f"Targeting v1 Base URL: {v1_base_url_main}")
    print(f"Targeting Deployment:  {main_deployment}")
    
    try:
        client_main = OpenAI(
            api_key=os.getenv("AZURE_MAIN_API_KEY"),
            base_url=v1_base_url_main
        )
        
        response_main = client_main.chat.completions.create(
            model=main_deployment,
            messages=[{"role": "user", "content": "Say: 'Main mentor connection successful!'"}]
        )
        print(f"✅ SUCCESS: {response_main.choices[0].message.content}")
        
    except Exception as e:
        print(f"❌ FAILED. Error details:\n{e}")

if __name__ == "__main__":
    test_azure_connections()