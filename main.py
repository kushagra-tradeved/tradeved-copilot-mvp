import sys
from src.router import analyze_conversation_frame
from src.guardrails import check_compliance_violation
from src.mentor_voice import generate_mentor_reply

def run_mvp_loop():
    print("=== Tradeved AI Mentor Co-Pilot MVP Terminal Activated ===")
    print("Type 'exit' to terminate the session.\n")
    
    # In-memory session chat storage
    chat_history = []
    
    while True:
        user_input = input("Mentee: ")
        if user_input.strip().lower() == "exit":
            print("Session closed safely.")
            sys.exit()
            
        chat_history.append({"role": "user", "content": user_input})
        
        # Format history string for the router
        formatted_history = "\n".join([f"{m['role']}: {m['content']}" for m in chat_history[-4:]])
        
        # Phase 1: Run GPT-5.4 mini Evaluation Router
        evaluation = analyze_conversation_frame(formatted_history)
        
        # Phase 2: Intercept via Compliance Guardrails
        guard_check = check_compliance_violation(evaluation)
        if guard_check["violation"]:
            reply = guard_check["fallback_response"]
            print(f"\n[System Guardrail Intercepted: {evaluation['compliance_risk']}]")
        else:
            # Phase 3: Run GPT-5.4 Generative Mentor Voice
            reply = generate_mentor_reply(chat_history, evaluation)
            
        print(f"\nMentor: {reply}\n")
        chat_history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    run_mvp_loop()