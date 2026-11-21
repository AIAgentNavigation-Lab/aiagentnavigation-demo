# AIAgentNavigation: Demonstration Only
# This is fictional test software, not the actual research engine.

def check_policy(action, approved):
    if not approved:
        return "DENIED: Approval is required."
    return f"PERMITTED: {action}"

if __name__ == "__main__":
    print("AIAgentNavigation - Practice Version 0.1.0")
    print(check_policy("Send research invitation", False))
    print(check_policy("Review synthetic research data", True))
