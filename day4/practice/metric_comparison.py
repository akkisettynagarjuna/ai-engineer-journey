import math

from sklearn.metrics import (mean_absolute_error,mean_squared_error)

actual = [50000, 60000, 70000]

# predicted = [49000, 59000, 150000]
# Practicals
# predicted = [49000, 59000, 71000]
predicted = [49000, 59000, 300000]
# Which metric increased the most?
# MSE increased the most because it squares every prediction error.
# When the prediction error becomes very large,
# its square becomes much larger.
# Therefore, MSE penalizes large mistakes much more heavily than MAE and RMSE.

mae = mean_absolute_error(actual, predicted)

mse = mean_squared_error(actual, predicted)

rmse = math.sqrt(mse)

print("MAE :", mae)
print("MSE :", mse)
print("RMSE :", rmse)

# Theory Questions
# What does MAE measure?
# Average Absolute Prediction Error / Average prediction mistake.
# What does MSE measure?
# Average Squared Prediction Error.
# Why does MSE punish large mistakes more?
# Because squaring makes large errors grow much faster than small errors.
# What is RMSE?
# RMSE is the square root of MSE, bringing the error back to the original unit.
# Which metric would you use to explain model performance to a business user? Why?
# MAE is generally easier to explain because it directly represents the average prediction error.
# RMSE is preferred when large prediction errors are more important and should receive greater attention.