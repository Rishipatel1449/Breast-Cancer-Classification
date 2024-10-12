# Breast Cancer Classification - By Rishi Patel

## Introduction
Breast cancer is one of the most prevalent cancers among women, making early detection crucial for improving survival rates. Traditional diagnostic methods such as mammography and biopsy can be slow and susceptible to errors. This project leverages machine learning to automate the detection process, analyze extensive datasets, and enhance accuracy, leading to faster and more reliable diagnoses that can significantly improve patient outcomes.

## Dataset Features

The dataset consists of several features that provide critical information for diagnosing breast tumors:

1. **ID**: A unique identifier for each patient, used for distinguishing data points.
  
2. **Diagnosis**: The target variable indicating whether a tumor is malignant (M) or benign (B), serving as the foundation for predictive modeling.

### Mean Value Measurements
3. **Radius Mean**: Average size of the tumor; larger radii may indicate more aggressive tumors.

4. **Texture Mean**: Variation in pixel intensity in the tumor image; irregular textures are typically associated with malignant tumors.

5. **Perimeter Mean**: Total length around the tumor; larger perimeters often correlate with malignancy.

6. **Area Mean**: Size of the tumor; larger areas generally suggest more aggressive or malignant growths.

7. **Smoothness Mean**: Regularity of tumor edges; benign tumors tend to have smoother edges compared to malignant ones.

8. **Compactness Mean**: Assess how tightly tumor cells are packed; lower compactness values are indicative of malignancy.

9. **Concavity Mean**: Degree of inward curvature of the tumor’s boundary; more severe concavities are indicative of malignancy.

10. **Concave Points Mean**: Quantifies the irregularity of the tumor; a higher count of concave points is associated with malignant tumors.

11. **Symmetry Mean**: Measures the symmetry of the tumor; benign tumors are typically more symmetrical.

12. **Fractal Dimension Mean**: Complexity of the tumor's boundary; higher values suggest more irregular shapes, which are common in malignant tumors.

### Standard Error Measurements
13. **Radius SE**: Reliability of the radius mean; lower values indicate consistent measurements.

14. **Texture SE**: Variability in texture measurements; higher values might suggest malignancy.

15. **Perimeter SE**: Consistency of perimeter measurements; significant variation can indicate irregular growth patterns.

16. **Area SE**: Variability in area measurements; inconsistencies may indicate more aggressive tumors.

17. **Smoothness SE**: Variation in smoothness; malignant tumors typically exhibit less regular growth.

18. **Compactness SE**: Assess variability in compactness; higher variation may suggest irregular shapes.

19. **Concavity SE**: Variation in concavity severity; higher values can indicate irregular tumor shapes.

20. **Concave Points SE**: Variability in the number of concave points; higher variation often suggests malignancy.

21. **Symmetry SE**: Consistency of symmetry measurements; greater variation indicates potential malignancy.

22. **Fractal Dimension SE**: Variability in boundary complexity; higher values suggest complex growth patterns associated with malignant tumors.

### "Worst" or Largest Value Measurements
23. **Radius Worst**: Largest observed radius; higher values indicate potential malignancy.

24. **Texture Worst**: Extreme texture deviation; more irregularity can suggest malignancy.

25. **Perimeter Worst**: Largest perimeter value; indicative of aggressive growth.

26. **Area Worst**: Largest recorded tumor area; typically associated with malignancy.

27. **Smoothness Worst**: Indicates worst-case edge irregularities; highly irregular edges may signal malignancy.

28. **Compactness Worst**: Extreme compactness value; lower values often point to malignancy.

29. **Concavity Worst**: Largest concavity value; significant inward curvature is common in malignant tumors.

30. **Concave Points Worst**: Largest count of concave points; more concave points often indicate malignancy.

31. **Symmetry Worst**: Worst symmetry value; malignant tumors typically display significant asymmetry.

## Model Used: Logistic Regression
In this project, I utilized the **Logistic Regression** model, which is effective for binary classification tasks. This statistical method models the probability of a binary outcome based on one or more predictor variables. Its interpretability and efficiency with medical data make it a suitable choice for predicting whether a tumor is malignant or benign.

## Results
To optimize the model's performance, I applied **feature scaling** using **StandardScaler** to standardize the dataset features, ensuring equal contribution to the distance calculations inherent in logistic regression. This step enhances convergence during model training.

I divided the dataset into training and testing sets, allocating **67%** of the data for training and **33%** for testing. This division allows for robust evaluation of the model's performance on unseen data.

The logistic regression model achieved an impressive overall prediction accuracy of **97.8%** on the test dataset. This high accuracy demonstrates the model's effectiveness in distinguishing between malignant and benign tumors, highlighting the potential of machine learning to enhance breast cancer diagnosis.
