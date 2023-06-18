install:
    poetry install

run:
    uvicorn app.main:app --reload
