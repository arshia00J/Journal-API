from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date


app = FastAPI()


class Journal(BaseModel):
    title: str
    content: str
    nowdate: date


journals: Journal = []


@app.get("/entries")
def get_all():
    return [{"id": idx, "entry": entry} for idx, entry in enumerate(journals)]


@app.post("/entries")
def create_journal(new: Journal):
    journals.append(new)
    return new


@app.put("/entries/{id}")
def update_journal(id: int, up_journal: Journal):
    if id >= len(journals) or id < 0:
        raise HTTPException(status_code=404, detail="Entry not found")
    journals[id] = up_journal
    return up_journal


@app.delete("/entries/{id}")
def delete_entry(id: int):
    if id >= len(journals) or id < 0:
        raise HTTPException(status_code=404, detail="Entry not found")
    journals.pop(id)
    return {"message": "Entry deleted"}
