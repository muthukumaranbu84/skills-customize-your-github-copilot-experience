#!/usr/bin/env python3
"""Starter code: simple notes manager using SQLAlchemy and SQLite.

Usage examples:
  python starter-code.py create --title "Test" --content "Hello"
  python starter-code.py list
  python starter-code.py get --id 1
  python starter-code.py update --id 1 --title "New"
  python starter-code.py delete --id 1
"""
from __future__ import annotations

import argparse
from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = "sqlite:///notes.db"

Base = declarative_base()


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:  # pragma: no cover - simple repr
        return f"<Note id={self.id} title={self.title!r}>"


engine = create_engine(DB_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def create_note(title: str, content: str) -> Note:
    session = SessionLocal()
    try:
        note = Note(title=title, content=content)
        session.add(note)
        session.commit()
        session.refresh(note)
        return note
    finally:
        session.close()


def list_notes() -> list[Note]:
    session = SessionLocal()
    try:
        return session.query(Note).order_by(Note.created_at).all()
    finally:
        session.close()


def get_note(note_id: int) -> Optional[Note]:
    session = SessionLocal()
    try:
        return session.get(Note, note_id)
    finally:
        session.close()


def update_note(note_id: int, title: Optional[str], content: Optional[str]) -> Optional[Note]:
    session = SessionLocal()
    try:
        note = session.get(Note, note_id)
        if not note:
            return None
        if title is not None:
            note.title = title
        if content is not None:
            note.content = content
        session.commit()
        session.refresh(note)
        return note
    finally:
        session.close()


def delete_note(note_id: int) -> bool:
    session = SessionLocal()
    try:
        note = session.get(Note, note_id)
        if not note:
            return False
        session.delete(note)
        session.commit()
        return True
    finally:
        session.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple notes manager using SQLite and SQLAlchemy")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_create = sub.add_parser("create")
    p_create.add_argument("--title", required=True)
    p_create.add_argument("--content", required=True)

    p_list = sub.add_parser("list")

    p_get = sub.add_parser("get")
    p_get.add_argument("--id", type=int, required=True)

    p_update = sub.add_parser("update")
    p_update.add_argument("--id", type=int, required=True)
    p_update.add_argument("--title")
    p_update.add_argument("--content")

    p_delete = sub.add_parser("delete")
    p_delete.add_argument("--id", type=int, required=True)

    return parser.parse_args()


def main() -> None:
    init_db()
    args = parse_args()

    if args.cmd == "create":
        note = create_note(args.title, args.content)
        print(f"Created: id={note.id} title={note.title}")
    elif args.cmd == "list":
        notes = list_notes()
        if not notes:
            print("No notes found.")
        for n in notes:
            print(f"{n.id}: {n.title} ({n.created_at.isoformat()})")
    elif args.cmd == "get":
        note = get_note(args.id)
        if not note:
            print("Note not found.")
        else:
            print(f"{note.id}: {note.title}\n{note.content}")
    elif args.cmd == "update":
        note = update_note(args.id, args.title, args.content)
        if not note:
            print("Note not found.")
        else:
            print(f"Updated: {note.id}: {note.title}")
    elif args.cmd == "delete":
        ok = delete_note(args.id)
        print("Deleted." if ok else "Note not found.")


if __name__ == "__main__":
    main()
