

import matplotlib.pyplot as plt

sedans_miles_driven = 10_000

sedans_current_mpg = 20
sedans_future_mpg = 50

sedans_gallons_used = []
sedans_gallons_saved = []

for mpg in range(sedans_current_mpg, sedans_future_mpg+1):
    sedans_gallons_used.append(sedans_miles_driven/mpg)
    sedans_gallons_saved.append( sedans_miles_driven/sedans_current_mpg - sedans_miles_driven/mpg)


suvs_miles_driven = 10_000

suvs_current_mpg = 10
suvs_future_mpg = 20

suvs_gallons_used = []
suvs_gallons_saved = []

for mpg in range(suvs_current_mpg, suvs_future_mpg+1):
    suvs_gallons_used.append(suvs_miles_driven/mpg)
    suvs_gallons_saved.append( suvs_miles_driven/suvs_current_mpg - suvs_miles_driven/mpg)


plt.plot(range(sedans_current_mpg, sedans_future_mpg+1), sedans_gallons_used, label="sedans gallons used" )
plt.plot(range(sedans_current_mpg, sedans_future_mpg+1), sedans_gallons_saved, label="sedans gallons saved" )
plt.plot(range(suvs_current_mpg, suvs_future_mpg+1), suvs_gallons_used, label="suvs gallons used" )
plt.plot(range(suvs_current_mpg, suvs_future_mpg+1), suvs_gallons_saved, label="suvs gallons saved" )
plt.legend()
plt.xlabel("mpg")
plt.ylabel("gallons")

plt.show()