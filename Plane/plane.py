class plane:
   def __init__(self, icao_code, latitude, longitude, altitude, last_time_reported, plane_callsign, is_on_ground):
      self.icao_code = icao_code
      self.latitude = latitude
      self.longitude = longitude
      self.altitude = altitude
      self.plane_callsign = plane_callsign
      self.last_time_reported = last_time_reported
      self.is_on_ground = is_on_ground


