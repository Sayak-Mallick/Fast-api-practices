import time
import asyncio

def sync_task(name):
  print(f"Synchronous task: {name} started")
  time.sleep(2)
  print(f"Synchronous task: {name} completed.")


sync_task("Task 1")
sync_task("Task 2")
sync_task("Task 3")


def cool_time():
  print("wait for 2 seconds");
  time.sleep(2)

cool_time()

async def async_tasks(name):
  print(f"Asynchronous task: {name} started")
  await asyncio.sleep(2)
  print(f"Asynchronous task: {name} completed.")


async def main():
  await asyncio.gather(
    async_tasks("Task 1"),
    async_tasks("Task 2"),
    async_tasks("Task 3")
  )


asyncio.run(main())