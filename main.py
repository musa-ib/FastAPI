from fastapi import FastAPI
from Routers import amicableSumRouter, curiousRouter, PrimesRouter, StrngRouter,triangleRouter,TruncateablePrimesRouter,LarPanPrimeRouter,calRouter
app = FastAPI()


app.include_router(amicableSumRouter.router)
app.include_router(curiousRouter.router)
app.include_router(PrimesRouter.router)
app.include_router(StrngRouter.router)
app.include_router(triangleRouter.router)
app.include_router(TruncateablePrimesRouter.router)
app.include_router(LarPanPrimeRouter.router)
app.include_router(calRouter.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",reload=True)

    