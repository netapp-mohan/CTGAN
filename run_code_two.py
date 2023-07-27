from ctgan import CTGAN
from ctgan import load_demo
import pandas as pd
import os
import time 
import gc
gc.enable()

os.environ['OMP_NUM_THREADS']='1'
os.environ['GOTO_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']= '1'

real_data = load_demo()

#all_columns = real_data.columns.tolist()
#discrete_columns = [col for col in all_columns]
discrete_columns = ['3','4','5','25','26','27','29','30','34','35','36','41','73','80','86','102']

ctgan = CTGAN(epochs=1, verbose=True)
ctgan.fit(real_data, discrete_columns)


# Start generating samples
desired_file_size_gb = 1  # Desired file size per iteration in GB
desired_file_size_bytes = desired_file_size_gb * 1024 * 1024 * 1024

# Create a directory to store the generated samples
os.makedirs('generated_samples', exist_ok=True)

# Start generating samples
total_files = 0

while total_files < 10:
    
    # Generate 1000 samples
    samples = ctgan.sample(2500000)

    # Save the samples to a file
    filename = f'generated_samples/samples_{total_files + 1}.csv'
    samples.to_csv(filename, index=False)

    # Get the file size
    file_size_bytes = os.path.getsize(filename)

    # If the file size exceeds the desired size, remove the file and skip to the next iteration
    if file_size_bytes > desired_file_size_bytes:
        os.remove(filename)
        print(f'Skipped sample {total_files + 1} due to file size exceeding {desired_file_size_gb} GB')
        continue

    # Increment the total files count
    total_files += 1

    print(f'Generated samples {total_files}. File size: {file_size_bytes} bytes.')

print('Generated 10 GB of data.')