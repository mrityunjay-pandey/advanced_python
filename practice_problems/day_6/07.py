import asyncio

async def accumulate():
    total = 0
    while True:
        value = await receive_value()  # Await the next value
        total += value
        print(f"Accumulated total: {total}")
        yield total

async def receive_value():
    # Simulate receiving a value asynchronously
    value = await get_next_value()
    return value

async def get_next_value():
    # Simulate fetching the next value asynchronously
    # For demonstration, we'll yield some example values
    for value in range(1, 6):
        await asyncio.sleep(1)  # Simulate some async operation
        yield value

async def main():
    async for total in accumulate():
        pass

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
