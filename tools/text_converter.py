"""Text converter tool: word count, character count, and text reversal."""


def process_text(command: str) -> str:
    """Process a text command: 'wordcount:<text>', 'charcount:<text>', or 'reverse:<text>'.
    
    Examples:
        process_text('wordcount: hello world') -> '2 words'
        process_text('charcount: abc') -> '3 characters'
        process_text('reverse: hello') -> 'olleh'
    """
    try:
        if ":" not in command:
            return "Invalid format. Use 'wordcount:<text>', 'charcount:<text>', or 'reverse:<text>'"
        
        cmd_type, text = command.split(":", 1)
        cmd_type = cmd_type.strip().lower()
        text = text.strip()
        
        if cmd_type == "wordcount":
            count = len(text.split())
            return f"Word count: {count}"
        
        elif cmd_type == "charcount":
            count = len(text)
            return f"Character count: {count}"
        
        elif cmd_type == "reverse":
            reversed_text = text[::-1]
            return f"Reversed: {reversed_text}"
        
        else:
            return f"Unknown command: {cmd_type}. Use 'wordcount', 'charcount', or 'reverse'."
    
    except Exception as e:
        return f"Error processing text: {e}"
