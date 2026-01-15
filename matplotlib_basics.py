import matplotlib.pyplot as plt

# Line Plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 25, 40]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# Bar Chart
names = ["A", "B", "C"]
marks = [70, 85, 90]

plt.bar(names, marks)
plt.title("Bar Chart Example")
plt.show()
