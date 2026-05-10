with open('.env') as f:
    for line in f:
        if 'ANTHROPIC_API_KEY' in line:
            key = line.strip().split('=', 1)[1]
            print(f"Key found: {key[:20]}...")
            
import anthropic
client = anthropic.Anthropic(api_key=key)

# Test it
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=10,
    messages=[{"role": "user", "content": "Say hi"}]
)
print("✅ API key works!")
