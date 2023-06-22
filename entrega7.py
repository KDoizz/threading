# import threading
# import time
# from PIL import Image
# import matplotlib.pyplot as plt

# # Open an image file
# img = Image.open('original.jpg')
# img = img.convert("RGB")

# d = img.getdata()

# new_image = [None]*len(d)

# # Define a function for the thread
# def change_color(start, end, index_start):
#     for i in range(start, end):
#         item = d[i]
#         # change all white (also shades of whites)
#         # pixels to yellow
#         if item[0] in list(range(200, 256)):
#             new_image[index_start] = ((0, 0, 255))  # (red, green, blue) for blue color
#         else:
#             new_image[index_start] = item
#         index_start += 1

# # Define a function to measure execution time
# def measure_execution_time(num_threads):
#     start_time = time.time()

#     threads = []
#     chunk_size = len(d) // num_threads
#     index_start = 0

#     # Create threads
#     for i in range(num_threads):
#         start = i * chunk_size
#         end = start + chunk_size
#         thread = threading.Thread(target=change_color, args=(start, end, index_start))
#         threads.append(thread)
#         index_start += chunk_size

#     # Start threads
#     for thread in threads:
#         thread.start()

#     # Wait for all threads to complete
#     for thread in threads:
#         thread.join()

#     # Update image data
#     img.putdata(new_image)

#     # Save new image
#     img.save(f'output_{num_threads}.jpg')

#     end_time = time.time()
#     execution_time = end_time - start_time
#     return execution_time

# # Define the range of number of threads to test
# num_threads_range = range(1, 9)

# # Measure execution time for different number of threads
# execution_times = []
# for num_threads in num_threads_range:
#     execution_time = measure_execution_time(num_threads)
#     execution_times.append(execution_time)

# # Plot the graph
# plt.plot(num_threads_range, execution_times)
# plt.xlabel('Number of Threads')
# plt.ylabel('Execution Time (seconds)')
# plt.title('Execution Time vs Number of Threads')
# plt.show()

# # Find the best number of threads with the minimum execution time
# best_num_threads = num_threads_range[execution_times.index(min(execution_times))]
# print(f"The best number of threads is: {best_num_threads}")


import threading
import time
from PIL import Image
import matplotlib.pyplot as plt

# Open an image file
img = Image.open('original.jpg')
img = img.convert("RGB")

d = img.getdata()

new_image = [None]*len(d)

# Define a function for the thread
def change_color(start, end, index_start):
    for i in range(start, end):
        item = d[i]
        # change all white (also shades of whites)
        # pixels to yellow
        if item[0] in list(range(200, 256)):
            new_image[index_start] = ((0, 0, 255))  # (red, green, blue) for blue color()

# Define the range of resolutions to test
resolutions = [(180, 120), (360, 240), (720, 480), (1440, 960)]

# Define the number of threads to use
num_threads = 3

# Measure execution time for different resolutions
execution_times = []
for resolution in resolutions:
    img_resized = img.resize(resolution)

    d_resized = img_resized.getdata()

    new_image_resized = [None]*len(d_resized)

    start_time = time.time()

    # Create threads
    threads = []
    chunk_size = len(d_resized) // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size
        thread = threading.Thread(target=change_color, args=(start, end, start))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

# Calculate the speed-up
speed_ups = [execution_times[0] / t for t in execution_times]

# Plot the graph
plt.plot([r[0] * r[1] for r in resolutions], speed_ups)
plt.xlabel('Resolution (pixels)')
plt.ylabel('Speed-Up')
plt.title('Speed-Up vs Resolution')
plt.show()
