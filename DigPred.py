import os
import tkinter as tk
from tkinter import messagebox
import numpy as np
import tensorflow as tf
from PIL import Image, ImageDraw

class DigitPredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MNIST Interactive Digit Predictor")
        self.root.resizable(False, False)
        
        # Load the pre-trained neural net file
        if not os.path.exists('mnist_model.h5'):
            messagebox.showerror("Error", "Missing 'mnist_model.h5'. Run 'train_mnist.py' first!")
            self.root.destroy()
            return
        self.model = tf.keras.models.load_model('mnist_model.h5')
        
        # Dimensions for drawing layout canvas window 
        self.canvas_size = 280 
        
        # 1. Title Label Banner Layout
        tk.Label(root, text="Draw a digit (0-9) inside the grid box:", font=("Arial", 11, "bold")).pack(pady=10)
        
        # 2. Interactive Painting Canvas Element
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="black", highlightthickness=1, highlightbackground="gray")
        self.canvas.pack(padx=20, pady=5)
        
        # Bind mouse movement gestures to drawing methods
        self.canvas.bind("<B1-Motion>", self.draw_pixels)
        
        # Create an underlying invisible PIL Image asset matching the canvas background dimensions
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), "black")
        self.draw = ImageDraw.Draw(self.image)
        
        # 3. Output Response Status Indicator Label
        self.prediction_lbl = tk.Label(root, text="Prediction: —", font=("Arial", 16, "bold"), fg="darkblue")
        self.prediction_lbl.pack(pady=10)
        
        # 4. Interactive Controller Buttons Frame Row
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10, fill=tk.X)
        
        tk.Button(btn_frame, text="🔮 Predict Digit", command=self.predict_digit, font=("Arial", 10, "bold"), bg="#add8e6", fg="black").pack(side=tk.LEFT, padx=25, expand=True)
        tk.Button(btn_frame, text="🔄 Clear Screen", command=self.clear_canvas, font=("Arial", 10), bg="#dcdcdc").pack(side=tk.RIGHT, padx=25, expand=True)

    def draw_pixels(self, event):
        """Draws onto the UI canvas and synchronizes pixels into the grayscale PIL image matrix."""
        r = 10 # Pen stroke size thickness index mapping
        x, y = event.x, event.y
        # Draw on visible UI layout
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="white", outline="white")
        # Mirror drawing track to data pixel matrix frame
        self.draw.ellipse([x-r, y-r, x+r, y+r], fill="white", outline="white")

    def clear_canvas(self):
        """Flushes pixel memory stores to start clean painting frames."""
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), "black")
        self.draw = ImageDraw.Draw(self.image)
        self.prediction_lbl.config(text="Prediction: —")

    def predict_digit(self):
        """Downsamples drawn tracking arrays to 28x28 and runs predictive evaluation arrays."""
        # 1. Downscale drawn canvas frame directly into standard 28x28 MNIST dimensional parameters
        img_resized = self.image.resize((28, 28), Image.Resampling.LANCZOS)
        
        # 2. Transmute image object arrays into a clean floating analytics numpy matrix arrays
        img_array = np.array(img_resized)
        
        # 3. Standardize and normalize bounds to mirror training vector weights scaling parameters
        img_array = img_array / 255.0
        
        # 4. Reshape dimensions from (28, 28) into matching network inputs structural array layout: (1, 28, 28)
        img_feed = np.expand_dims(img_array, axis=0)
        
        # 5. Extract forward pass analytics arrays predictions evaluations
        predictions = self.model.predict(img_feed)
        best_choice = np.argmax(predictions[0])
        confidence = predictions[0][best_choice] * 100
        
        # Update output layout parameters labels structures
        self.prediction_lbl.config(text=f"Prediction: {best_choice} ({confidence:.1f}%)")

if __name__ == "__main__":
    window = tk.Tk()
    app = DigitPredictorApp(window)
    window.mainloop()
