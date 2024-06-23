import asyncio

async def filter_and_process(items, threshold):
    filtered_items = [item for item in items if item > threshold]
    for item in filtered_items:
        await process_item(item)

async def process_item(item):
    # Simulate processing each item asynchronously
    print(f"Processing item: {item}")
    await asyncio.sleep(1)  # Simulate some async operation

async def main():
    items = [3, 8, 1, 10, 5, 2, 7]
    threshold = 5
    await filter_and_process(items, threshold)

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
