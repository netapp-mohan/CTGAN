from ctgan import CTGAN
from ctgan import load_demo
import pandas as pd
import os
import time 
import gc
gc.enable()

real_data = load_demo()

# Names of the columns that are discrete
all_columns = real_data.columns.tolist()
discrete_columns = [col for col in all_columns]
#discrete_columns = ['3','4','5','25','26','27','29','30','34','35','36','41','73','80','86','102']
# columns to check for N -> 0 or 0 -> N : 41,73, 104, 
ctgan = CTGAN(epochs=1, batch_size= 64, verbose=True)
ctgan.fit(real_data, discrete_columns)

desired_size_gb = 100

# Convert the size to bytes
desired_size_bytes = desired_size_gb * 1024 * 1024 * 1024

# Create a directory to store the generated samples
os.makedirs('generated_samples', exist_ok=True)

# Start generating samples
total_size_bytes = 0
iteration = 1

while total_size_bytes < desired_size_bytes:
    # Generate 1000 samples
    samples = ctgan.sample(1000)

    # Save the samples to a file
    filename = f'generated_samples/samples_{iteration}.csv'
    samples.to_csv(filename, index=False)

    # Update the total size
    total_size_bytes += os.path.getsize(filename)

    print(f'Generated samples {iteration}. Total size: {total_size_bytes} bytes')

    # Wait for a few seconds before the next iteration
    time.sleep(5)

    iteration += 1

print('Generation stopped. Desired size reached.')

"""
# Create synthetic data
synthetic_data = ctgan.sample(1000)
df_out = pd.DataFrame(synthetic_data)
df_out.to_csv('sample_output1.csv', index = False)
"""