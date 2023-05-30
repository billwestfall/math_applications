import pandas as pd
from numpy.random import default_rng

rng = default_rng(12345)

diff_data = rng.normal(0, 1, size=100)
cumulative = np.add.accumulate(diff_data)

data_series = pd.Series(diff_data)
print(data_series)

data_frame = pd.DataFrame({
 "diffs": data_series,
 "cumulative": cumulative
})

print(data_frame)
