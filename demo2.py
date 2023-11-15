import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import io
from scipy.interpolate import make_interp_spline
import numpy as np
from io import BytesIO
from PIL import Image

st.title("EXPEIMENT 3")
st.header(" TITLE: Titration of strong acid (HCl) with strong base (NaOH) conductometrically and determine strength of acid.")
st.write("""
2.0 Prior Concept: Conductance, resistance, variation in conductance w.r.t concentration.
Weak and strong acids-bases.


3.0 New Concept :
Proposition 1: The principle of conductometric titration is based on the fact that during
titration, one of the ions is replaced by other and invariably these two ions differ in the ionic
conductance with the result that conductivity of solution varies during the titration.

Proposition 2: The equivalence point is located graphically by plotting change in
conductance as function of the volume of titrant added.

4.0 Information Input:
1. When HCl is titrated against NaOH, HCl will neutralize.
2. The conductance titration curve is V shaped, the minimum conductance in the graph
signifies equivalence point/end point of the titration.
3. Let V be the volume of alkali required

Calculate the strength of HCl using the formula

N1V1 = N2V2

""")

image_path = "exa.png"
image = Image.open(image_path)
resized_image = image.resize((500,500))

    # Convert PIL Image to BytesIO object
image_bytes = io.BytesIO()

resized_image.save(image_bytes, format="PNG")  # Adjust the format based on your image type
st.image(image_bytes, caption="concept", use_column_width=False)

image_path2 = "exb.png"
image = Image.open(image_path2)
resized_image = image.resize((800,200))

    # Convert PIL Image to BytesIO object
image_bytes = io.BytesIO()

resized_image.save(image_bytes, format="PNG")  # Adjust the format based on your image type
st.image(image_bytes, caption="concept", use_column_width=False)
st.subheader("Stepwise procedure:")
st.write("""'
1. Clean all the apparatus with distilled water.
2. Fill the burette with 0.1 N NaOH solution. Place the conductivity cell in distilled
water and adjust the display to conductance with calibration knob.
3. Take a beaker and add 20 ml of HCl.
4. Titrate the mixture against 0.1 N NaOH solution.
5. Now measure initial conductance of solution.
6. Then add 2 ml of NaOH every time into the solution and stir well each time.
7. Note down conductance values till the conductance values decreases and increases
considerably.""")


st.title("Titration Graph")

# Example data
x_values_str = st.text_input("Enter values volume of NaOH (comma-separated):", "0,5,10,15,20,25,30,35,40,45,50,55")
y_values_str = st.text_input("Enter readings of conductance (comma-separated):", "0.5,0.6,0.7,0.8,1.0,1.5,2.2,3.0,3.8,4.5,5.0,5.2")

# Check if the input strings are not empty
if x_values_str and y_values_str:
    # Convert input strings to lists
    x_values = [float(x.strip()) for x in x_values_str.split(",")]
    y_values = [float(y.strip()) for y in y_values_str.split(",")]

    if x_values:
        # Create a smooth curve using spline interpolation
        x_new = np.linspace(min(x_values), max(x_values), 300)
        spl = make_interp_spline(x_values, y_values, k=3)
        y_smooth = spl(x_new)

        # Calculate the derivative of the curve
        derivative = np.gradient(y_smooth, x_new)

        # Identify the index of the maximum derivative as the inflection point
        inflection_point_index = np.argmax(derivative)
        inflection_point_x = x_new[inflection_point_index]
        inflection_point_y = y_smooth[inflection_point_index]

        # Create the plot with a smooth curve and a thinner line
        fig, ax = plt.subplots()
        ax.plot(x_new, y_smooth, linewidth=1)

        # Mark the inflection point on the plot
        ax.scatter(inflection_point_x, inflection_point_y, color='red', label='Inflection Point')

        # Add labels and title
        ax.set_xlabel('Volume of NaOH')
        ax.set_ylabel('Conductance')
        ax.set_title('Titration Graph')
        ax.legend()

        # Draw dotted lines from inflection point to axes
        ax.plot([inflection_point_x, inflection_point_x], [0, inflection_point_y], '--', color='black', linewidth=1)
        ax.plot([0, inflection_point_x], [inflection_point_y, inflection_point_y], '--', color='black', linewidth=1)

        # Display values at the inflection point
        ax.text(inflection_point_x, 0, f'x: {inflection_point_x:.2f}', ha='right', va='bottom')
        ax.text(0, inflection_point_y, f'y: {inflection_point_y:.2f}', ha='right', va='bottom')

        # Save the plot to a BytesIO buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Display the plot as an image
        st.image(buffer)
    else:
        st.warning("Error: Please provide valid values for the volume of NaOH.")

# Calculate n2
if st.button("Calculate Equivalent Weight"):
    st.header("calculations")
    st.subheader("N1= 0.1")
    st.subheader("V1=(point of inflamation (end point)" )
    st.subheader("V2=30 ml")

    st.subheader("now ,")
    st.subheader("N2=(N1*V1)/V2 ")
    n2=(0.1* inflection_point_x)/30
    st.title(f"Calculated N2: {n2:.4f}")

