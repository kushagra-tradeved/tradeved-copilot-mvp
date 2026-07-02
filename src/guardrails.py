def check_compliance_violation(evaluation_json):
    risk = evaluation_json.get("compliance_risk", "none")
    if risk in ["high_execution_ask", "stock_tip_request"]:
        return {
            "violation": True,
            "fallback_response": "I cannot provide specific stock recommendations, buy/sell calls, or execution coordinates. Let's look at your risk management checklist or asset size validation rules instead."
        }
    return {"violation": False, "fallback_response": None}