import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BmiCalulator:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")

        self.label_weight = tk.Label(master, text="Enter Weight (kg):")
        self.label_weight.pack()

        self.entry_weight = tk.Entry(master)
        self.entry_weight.pack()

        self.label_height = tk.Label(master, text="Enter Height (m):")
        self.label_height.pack()

        self.entry_height = tk.Entry(master)
        self.entry_height.pack()

        self.calculate_button = tk.Button(master, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

        self.user_data = []

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())

            # BMI Calculation
            bmi = round(weight / (height ** 2), 2)

            # Categorization
            category = self.get_category(bmi)

            # Display result
            messagebox.showinfo("BMI Result", f"Your BMI: {bmi}\nCategory: {category}")

            # Save data
            self.user_data.append((weight, height, bmi))

            # Update data visualization
            self.update_visualization()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

    def get_category(self, bmi):
        # Define BMI categories
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal Weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def update_visualization(self):
        # Clear previous plot
        plt.clf()

        # Extract data for plotting
        weights = [data[0] for data in self.user_data]
        heights = [data[1] for data in self.user_data]
        dates = range(1, len(self.user_data) + 1)

        # Plot weight over time
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(dates, weights, marker='o', linestyle='-', color='b')
        ax1.set_ylabel('Weight (kg)')
        ax1.set_title('Weight and BMI Over Time')

        # Plot BMI over time
        ax2.plot(dates, [data[2] for data in self.user_data], marker='o', linestyle='-', color='r')
        ax2.set_ylabel('BMI')
        ax2.set_xlabel('Measurement Number')

        # Embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = BmiCalulator(root)
    root.mainloop()