import asyncio
from Mikobot.state import State  # Import the State class

async def main():
    arq = await State.get_arq()  # ✅ Proper way to get the ARQ client
    response = await arq.query("Hello")
    print(response)

asyncio.run(main())  # ✅ Ensures it runs in an async environment
