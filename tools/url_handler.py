"""URL encoder and decoder tool."""
from urllib.parse import quote, unquote


def process_url(command: str) -> str:
    """Process URL commands: 'encode:<text>', 'decode:<url>', or 'info:<url>'.
    
    Examples:
        process_url('encode: hello world') -> 'hello%20world'
        process_url('decode: hello%20world') -> 'hello world'
        process_url('info: https://example.com') -> 'URL breakdown'
    """
    try:
        if ":" not in command:
            return "Invalid format. Use 'encode:<text>', 'decode:<text>', or 'info:<url>'"
        
        cmd_type, content = command.split(":", 1)
        cmd_type = cmd_type.strip().lower()
        content = content.strip()
        
        if cmd_type == "encode":
            encoded = quote(content, safe='')
            return f"Encoded: {encoded}"
        
        elif cmd_type == "decode":
            decoded = unquote(content)
            return f"Decoded: {decoded}"
        
        elif cmd_type == "info":
            from urllib.parse import urlparse
            parsed = urlparse(content)
            info = f"Scheme: {parsed.scheme}\nHost: {parsed.netloc}\nPath: {parsed.path}\nQuery: {parsed.query}"
            return f"URL Info:\n{info}"
        
        else:
            return f"Unknown command: {cmd_type}. Use 'encode', 'decode', or 'info'."
    
    except Exception as e:
        return f"Error processing URL: {e}"
