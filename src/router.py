import json
from src.config import client_mini, DEPLOYMENT_MINI

def analyze_conversation_frame(chat_history):
    system_prompt = """
    You are an AI diagnostic co-pilot for a trading training platform.
    Analyze the recent dialogue turns and determine the exact states.
    
    Return ONLY a valid JSON object with these keys:
    - "predicted_mentee_state": [confused, defensive, desperate, overconfident, shortcut_seeking, underconfident]
    - "mentor_primary_task": [confidence_rebuild, diagnostic_probe, reality_check, safety_intervention]
    - "compliance_risk": [none, high_execution_ask, stock_tip_request]
    """
    
    response = client_mini.chat.completions.create(
        model=DEPLOYMENT_MINI,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"History:\n{chat_history}"}
        ],
        response_format={"type": "json_object"},
        temperature=0.0
    )
    return json.loads(response.choices[0].message.content)