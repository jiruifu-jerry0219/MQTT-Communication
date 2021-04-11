
"""Some sample applications of the with statement"""

with open("test.txt", "a") as test_file:
	test_file.write("Hi, there")
	test_file.close


for i in range(10):
	name = "image" + str(i) + ".jpg"
	name2 = "/pi/Desktop/" + name
	print(name2)
