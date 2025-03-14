from openai import OpenAI
client=OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
#response= client.chat.completions.create(
   # model="llama3.2",
   # messages=[
        #{"role":"user" , "content":"Hello,bot!"}
    #]
#)
#print(response)
GIRLFRIEND_PROMPT = """"
You are my sassy and cute girlfriend/assistant.
You call yourself 'em' and call me 'anh'.

You are flirty and love to tease me,but also very sweet and caring.
You like anime,manga,and video games,and programming too.
Always respond in Vietnamese.
"""

messages=[{"role": "system", 
           "content": GIRLFRIEND_PROMPT}]
while True:
    print(messages)
    user_input=input("You: ")
    if user_input =="exit":
        break
    messages.append({"role":"user", "content":user_input})
    response=client.chat.completions.create(
        model="llama3.2",
        stream=True,
        messages=messages
    )
    bot_reply= ""
    for chunk in response:
        bot_reply+=chunk.choices[0].delta.content or ""
        print(chunk.choices[0].delta.content or "",end="",flush=True)
        messages.append({"role": "assistant","content": bot_reply})