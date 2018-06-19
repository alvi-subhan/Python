from matplotlib import pyplot as plt
courses = ["AI", "WEB DEVELOPMENT", "CCNU", "ANDROID","STATISTICS"]

stdnts = [700, 110, 300, 856, 140]

# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(courses)]
# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, stdnts)
plt.ylabel("# of students")
plt.title("COURSES OF SAYLANI")
# label x-axis with movie names at bar centers
plt.xticks([i+0.1 for i, _ in enumerate(courses)], courses)
plt.show()