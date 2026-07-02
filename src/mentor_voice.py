from src.config import client_main, DEPLOYMENT_MAIN

def generate_mentor_reply(chat_history, evaluation_json):
    task = evaluation_json.get("mentor_primary_task", "diagnostic_probe")
    state = evaluation_json.get("predicted_mentee_state", "confused")
    
    system_prompt = f"""
    You are an educational trading mentor. You never give tips or stock picks. 
    Your current primary task is: {task}. The user's psychological profile right now is: {state}.
    
    Instructions:
    - Ground your response in process, capital protection, and discipline.
    - Validate emotions naturally but immediately pivot to a concrete diagnostic framework.
    - End your reply with a single, highly actionable checkpoint question.
    """
    
    response = client_main.chat.completions.create(
        model=DEPLOYMENT_MAIN,
        messages=[
            {"role": "system", "content": system_prompt},
            *chat_history
        ],
        temperature=0.4
    )
    return response.choices[0].message.content