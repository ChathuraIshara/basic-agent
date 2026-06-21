"""Password generator and strength checker tool."""
import string
import random


def process_password(command: str) -> str:
    """Process password commands: 'generate:<length>', 'strength:<password>', or 'random:<type>'.
    
    Examples:
        process_password('generate: 12') -> generates 12-char password
        process_password('strength: MyPassword123!') -> checks password strength
        process_password('random: strong') -> generates strong random password
    """
    try:
        if ":" not in command:
            return "Invalid format. Use 'generate:<length>', 'strength:<password>', or 'random:<type>'"
        
        cmd_type, content = command.split(":", 1)
        cmd_type = cmd_type.strip().lower()
        content = content.strip()
        
        if cmd_type == "generate":
            try:
                length = int(content)
                if length < 4:
                    return "Password length must be at least 4"
                chars = string.ascii_letters + string.digits + string.punctuation
                pwd = ''.join(random.choice(chars) for _ in range(length))
                return f"Generated password ({length} chars): {pwd}"
            except ValueError:
                return "Length must be a number"
        
        elif cmd_type == "strength":
            score = 0
            feedback = []
            
            if len(content) >= 8:
                score += 1
            else:
                feedback.append("too short (< 8 chars)")
            
            if any(c.isupper() for c in content):
                score += 1
            else:
                feedback.append("no uppercase letters")
            
            if any(c.islower() for c in content):
                score += 1
            else:
                feedback.append("no lowercase letters")
            
            if any(c.isdigit() for c in content):
                score += 1
            else:
                feedback.append("no digits")
            
            if any(c in string.punctuation for c in content):
                score += 1
            else:
                feedback.append("no special characters")
            
            strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"][score]
            tips = ", ".join(feedback) if feedback else "excellent!"
            return f"Strength: {strength} ({score}/5) - {tips}"
        
        elif cmd_type == "random":
            pwd_type = content.lower()
            if pwd_type == "weak":
                pwd = ''.join(random.choices(string.ascii_lowercase, k=8))
            elif pwd_type == "medium":
                chars = string.ascii_letters + string.digits
                pwd = ''.join(random.choices(chars, k=12))
            elif pwd_type == "strong":
                chars = string.ascii_letters + string.digits + string.punctuation
                pwd = ''.join(random.choices(chars, k=16))
            else:
                return "Type must be 'weak', 'medium', or 'strong'"
            return f"Random {pwd_type} password: {pwd}"
        
        else:
            return f"Unknown command: {cmd_type}. Use 'generate', 'strength', or 'random'."
    
    except Exception as e:
        return f"Error processing password: {e}"
