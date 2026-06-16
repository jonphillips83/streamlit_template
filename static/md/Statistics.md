
# Statistics 101

## Measures of Central tendency

### Mean

$$\bar{x} = \frac{\sum x}{n}$$
```Python
import numpy as np

mean_val = np.mean(data) 
```

### Median

When in an ordered list:
$$\text{Position of Median} = \frac{n + 1}{2}$$
```Python
import numpy as np

median_val = np.median(data)
```

### Mode

Value(s) that occur most frequently.

There can be more than one mode or no mode.

## Measures of Spread

### Range

Difference between largest and smallest value
$$Range = max(x) - min(x)$$
```Python
import numpy as np

# peak to peak
data_range = np.ptp(data)
```

### Inter Quartile Range (ICR)

Measures the spread of the inner 50% of vales.

When in an ordered list:
$$Q_2 = median$$
$$Q_1 = \frac{n + 1}{4}$$
$$Q_3 = \frac{3(n + 1)}{4}$$
$$ICR = Q3 - Q1$$  
```Python
import numpy as np

q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)  # Median
q3 = np.percentile(data, 75) 
iqr = q3 - q1
```

### Standard Deviation

The typical distance of data values from the mean

$$s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n - 1}}$$
The sum of all values minus the mean, they are squared to make all the values positive. When the data is a sample the denominator is the number of values minus one, known as **Bessel's correction**. The whole calculation is square rooted to correct the metric after the earlier squaring. 

```Python
import numpy as np

# ddof = 1 (Bessel Correction)
std_sample = np.std(data, ddof=1)
```

## Graphing

### Histogram

### Boxplot

Min, Q1, Q2, Q3, Max

## Probability

The measure of how likely an event is to occur. Measured from 0 (impossible) to 1 (certain) 

### Theoretical Probability

$$P(A) = \frac{n(A)}{n(S)} =\frac {\text{\# Favourable Outcomes}}{\text{\# Possible Outcomes}}$$
### Experimental Probability

$$P(A) = \frac{n(A)}{n(S)} =\frac {\text{\# of Occurances}}{\text{\# of Trials}}$$
The experimental probability will converge on the theoretical probability as the number of trials increases.
### Probability Mass Function
Discrete
### Probability Density Function
Continuous


