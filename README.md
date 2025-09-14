# OIBSIP_pythonprogramming_project2

## BMI Calculator

### Objective  
The objective of this project is to build a BMI (Body Mass Index) Calculator in Python that helps users calculate their BMI based on weight and height inputs. The program also classifies the BMI into categories (Underweight, Normal, Overweight, or Obese) and provides relevant health advice.  

---

### Steps Performed  

1. **User Input with Validation**  
   - Prompt the user to enter their weight and choose a unit (kg or lbs).  
   - Prompt the user to enter their height and choose a unit (m or cm).  
   - Input validation ensures correct units and positive values.  

2. **Conversion to Standard Units**  
   - Weight in pounds (lbs) is converted to kilograms (kg).  
   - Height in centimeters (cm) is converted to meters (m).  

3. **BMI Calculation**  
   - Formula used:  

     ```
     BMI = Weight (kg) / (Height (m))^2
     ```

4. **Category Classification**  
   - Underweight: BMI < 18.5  
   - Normal weight: 18.5 ≤ BMI < 24.9  
   - Overweight: 25 ≤ BMI < 29.9  
   - Obesity: BMI ≥ 30  

5. **Advice and Visualization**  
   - Provides health advice based on the category.  
   - Displays an ASCII progress bar that visually represents the BMI value.  

---

### Tools and Technologies Used  
- Programming Language: Python 3  
- Libraries Used:  
  - `time` (for delays if needed)  
  - Standard I/O functions (`input`, `print`)  

---

### Outcome  
- Successfully calculates BMI based on user inputs.  
- Handles both metric and imperial units.  
- Provides category, health advice, and a visual ASCII progress bar.  
- Enhances user interaction through clear prompts and error handling.  
