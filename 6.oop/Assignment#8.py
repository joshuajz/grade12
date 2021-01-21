class convert:
    def __init__(self, measurement, m_type, guess):
        self.measurement = float(measurement)
        self.type = m_type
        self.guess = float(guess)

    def convert(self):
        conversions = {
            "km": ["mile(s)", 0.621371],
            "m": ["yard(s)", 1.09361],
            "cm": ["inch(es)", 0.393701],
            "kg": ["pound(s)", 2.20462],
            "liter": ["gallon(s)", 0.264172],
        }

        converted = conversions[self.type]
        new_measurement = converted[1] * self.measurement
        new_type = converted[0]

        return (
            f"You converted {self.measurement} {self.type} to {new_measurement} {new_type}",
            new_measurement,
        )

    def check_guess(self):
        x = self.convert()

        print(x[0])

        if self.guess > x[1]:
            comparison = "larger"
        elif self.guess < x[1]:
            comparison = "smaller"
        else:
            comparison = "equal to"

        print(
            f"Your Guess: {self.guess} | Correct Answer: {x[1]} | You were {comparison} the guess."
        )


x = convert(
    input("Measurement: "),
    input("Measurement Type (km, m, cm, kg, liter): "),
    input("Guess: "),
)

x.check_guess()