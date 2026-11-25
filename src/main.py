import asyncio
import uvicorn


async def main() -> None:
    uvicorn.run('src.app:get_app', port=8001, reload=True, factory=True)

if __name__ == '__main__':
    asyncio.run(main())
