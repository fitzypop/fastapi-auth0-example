install:
    poetry install

run:
    uvicorn example_api.main:app --reload
