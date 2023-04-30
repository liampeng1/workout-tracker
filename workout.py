
from datetime import datetime
from typing import List

class Workout:

  def __init__(self, date_time: datetime, input_string: str, notes: str) -> None:
    self.date_time = date_time
    self.input_string = input_string
    self.notes = notes

  @staticmethod
  def from_dict(source: dict):
    return Workout(source['date_time'], source['input_string'], source['notes'])

  def to_dict(self):
    return {
      'date_time': self.date_time,
      'input_string': self.input_string,
      'notes': self.notes
    }

class Run(Workout):

  def __init__(self, date_time: datetime, input_string: str, notes: str, distance_mi: float, duration_sec: int) -> None:
      super().__init__(date_time, input_string, notes)
      self.distance_mi = distance_mi
      self.duration_sec = duration_sec

  @staticmethod
  def from_dict(source: dict):
    return Run(source['date_time'], source['input_string'], source['notes'], source['distance_mi'], source['duration_sec'])

  def to_dict(self):
    d = super().to_dict()
    d['distance_mi'] = self.distance_mi
    d['duration_sec'] = self.duration_sec
    return d

class Lift:

  def __init__(self, lift_name: str, sets: List[int]) -> None:
    self.lift_name = lift_name
    self.sets = sets

  @staticmethod
  def from_dict(source: dict):
    return Lift(source['lift_name'], source['sets'])

  def to_dict(self):
    return {
      'lift_name': self.lift_name,
      'sets': self.sets
    }

class Gym(Workout):

  def __init__(self, date_time: datetime, input_string: str, notes: str, lifts: List[Lift]) -> None:
    super().__init__(date_time, input_string, notes)
    self.lifts = lifts

  @staticmethod
  def from_dict(source: dict):
    lifts = [Lift(lift_source) for lift_source in source['lifts']]
    return Gym(source['date_time'], source['input_string'], source['notes'], lifts)

  def to_dict(self):
    d = super().to_dict()
    d['distance_mi'] = self.distance_mi
    d['duration_sec'] = self.duration_sec
    return d
  