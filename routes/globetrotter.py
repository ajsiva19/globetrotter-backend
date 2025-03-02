from fastapi import APIRouter,HTTPException,Depends
from utils.database.db_connection import get_db
from sqlalchemy.orm import Session
from modals.globetrotter import Destination
from schemas.globetrotter import AnswerRequest
import random
globetrotter_router = APIRouter()

@globetrotter_router.get("/random-destination")
def get_random_destination(db: Session = Depends(get_db)):
    destinations = db.query(Destination).all()
    if not destinations:
        raise HTTPException(status_code=404, detail="No destinations available")
    destination = random.choice(destinations)
    options = [dest.city for dest in random.sample(destinations, min(4, len(destinations)))]
    if destination.city not in options:
        options[0] = destination.city
    random.shuffle(options)
    return {"clues": random.sample(destination.clues, 2), "options": options, "id": destination.id}

@globetrotter_router.post("/check-answer")
def check_answer(request: AnswerRequest, db: Session = Depends(get_db)):
    destination = db.query(Destination).filter(Destination.id == request.city).first()
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    correct = request.answer.lower() == destination.city.lower()
    return {"correct": correct, "fun_fact": random.choice(destination.fun_facts)}