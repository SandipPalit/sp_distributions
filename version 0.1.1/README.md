This is a statistical Python library,  to compute Mean and Standard deviation on of various Probability distributions,
 like _Gaussian Distribution_ and _Binomial distribution_. This package is developed by **Sandip Palit**.
 
Install statement: **_pip install sp_distributions_**
 
## **Import statement :**

Gaussian:  **_from sp_distributions import Gaussian_**

Binomial: **_from sp_distributions import Binomial_**

## **Initialise statement :**

Gaussian:  **_g=Gaussian(5,3)_**    (mu=5, sigma=3)

Binomial: **_b=Binomial(0.5,3)_**    (p=0.5, n=3)

## **Methods :**

**calculate_mean()**

_Function to calculate the mean of the data set._

Args: None

Returns: float

**calculate_stdev()**

_Function to calculate the standard deviation of the data set._

Args: None

Returns: float

**read_data_file()**

_Function to read in data from a txt file. The txt file should have one number (float) per line. After reading in the file, the mean and standard deviation are calculated_

Args: file_name (string)

Returns: None

**plot()**

_Function to output a plotting of the instance variable data using matplotlib pyplot library._

Args: None

Returns: None

**pdf():**

_Probability density function calculator for the gaussian distribution, on a specific point (x)._

Args: x (float)

Returns: float

**plot_pdf():**

_Function to plot the normalized graph of the data and a plot of the probability density function along the same range._

Args: n_spaces (int)

Returns: x values (list), y values (list)



_You can also add together two objects of a distribution by using **+** operator._