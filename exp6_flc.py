import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

# Input and output variables
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Fuzzy membership functions for temperature (°C)
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature['warm'] = fuzz.trimf(temperature.universe, [15, 25, 35])
temperature['hot'] = fuzz.trimf(temperature.universe, [30, 40, 40])

# Fuzzy membership functions for humidity (%)
humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['medium'] = fuzz.trimf(humidity.universe, [30, 50, 70])
humidity['high'] = fuzz.trimf(humidity.universe, [50, 100, 100])

# Fuzzy membership functions for fan speed (%)
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Fuzzy rules
rule1 = ctrl.Rule(temperature['cold'] and humidity['low'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['warm'] or humidity['medium'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'] or humidity['high'], fan_speed['high'])

# Control system setup
fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
fan_simulation = ctrl.ControlSystemSimulation(fan_ctrl)

# Pass test inputs
fan_simulation.input['temperature'] = 28
fan_simulation.input['humidity'] = 65

# Compute the output
fan_simulation.compute()
print(f"Calculated Fan Speed: {fan_simulation.output['fan_speed']:.2f}%")