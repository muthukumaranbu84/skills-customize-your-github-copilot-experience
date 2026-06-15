from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Note(BaseModel):
    id: int
    title: str
    content: str


notes = {}
next_id = 1


@app.get("/notes", response_model=List[Note])
def list_notes():
    return list(notes.values())


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return notes[note_id]


class NoteCreate(BaseModel):
    title: str
    content: str


@app.post("/notes", status_code=201, response_model=Note)
def create_note(payload: NoteCreate):
    global next_id
    note = Note(id=next_id, title=payload.title, content=payload.content)
    notes[next_id] = note
    next_id += 1
    return note


@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, payload: NoteCreate):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    note = Note(id=note_id, title=payload.title, content=payload.content)
    notes[note_id] = note
    return note


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes[note_id]
    return None


def main():
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
