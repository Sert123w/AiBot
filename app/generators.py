
'''from openai import AsyncOpenAI
import asyncio
import httpx
from config import AI_TOKEN

client = AsyncOpenAI(api_key=AI_TOKEN,
                     http_client=httpx.AsyncClient(proxies="http://логин:пороль@ip:порт",
                                                   transport=httpx.HTTPTransport(local_address="0.0.0.0")))


async def gpt_text(req, model):
    completion = await client.chat.completions.create(
        messages=[{"role": "user", "content": str(req)}],
        model=model
    )
    return {"response": completion.choices[0].message.content,
             "usage": completion.usage.total_tokens}
'''

async def gpt_text_test():
    return {"response": "Будет...",
             "usage": 75}
#asyncio.run(gpt_text("привет", "gpt-3.0"))

#async def gpt_image

async def gpt_image():
    return {"response": "https://images.wallpaperscraft.com/image/single/bridge_rocks_river_58661_2560x1600.jpg",
             "usage": 1}