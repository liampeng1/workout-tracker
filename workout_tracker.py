import json
from flask import Flask, request
from workout import Run, Workout
from datetime import datetime

from google.cloud import firestore

db = firestore.Client()

app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/add-workout')
def add_workout():
  workout_strings = request.args.get('workout').split('\n')
  workout_type = workout_strings[0].lower()
  if 'run' in workout_type:
    run = build_run(workout_strings)
    add_workout(run)
    d = run.to_dict()
    d['date_time'] = str(d['date_time'])
    return json.dumps(d)
  else:
    return f'Workout type: {workout_type} is not supported '

def build_run(workout_strings):
  run_dist, run_duration, notes = float(workout_strings[1]), int(workout_strings[2]), workout_strings[3]
  return Run(datetime.now(), '\n'.join(workout_strings), notes, run_dist, run_duration)

def add_workout(workout: Workout):
  doc_name = str(workout.date_time)
  db.collection('workouts').document(doc_name).set(workout.to_dict())