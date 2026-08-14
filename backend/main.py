from fastapi import FastAPI

aplicacion = FastAPI()


@aplicacion.get('/')
async def main():
    return {"message" : "Hello from astronomicaldatabase!"}
    

if __name__ == "__main__":
    main()
