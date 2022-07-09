class DriveBot:
  # Create a counter to keep track of how many robots were created
  counter = 0
  all_disabled = False
  latitude = -999999
  longitude = -999999

  def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
    self.motor_speed = motor_speed
    self.direction = direction
    self.sensor_range = sensor_range
    # Assign an `id` to the robot when it is constructed by incrementing the counter and assigning the value to `id`
    DriveBot.counter += 1
    self.id = DriveBot.counter

  def control_bot(self, new_speed, new_direction):
    self.motor_speed = new_speed
    self.direction = new_direction

  def adjust_sensor(self, new_sensor_range):
    self.sensor_range = new_sensor_range