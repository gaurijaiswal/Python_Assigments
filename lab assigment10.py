import matplotlib.pyplot as plt

companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Amdocs']
recruitment = [200, 180, 220, 150, 120]

# a) Bar Chart
plt.bar(companies, recruitment)
plt.title("Recruitment Data")
plt.show()

# b) Pie Chart
plt.pie(recruitment, labels=companies, autopct='%1.1f%%')
plt.show()

# c) Customized Pie Chart
plt.pie(recruitment, labels=companies, autopct='%1.1f%%', explode=[0,0,0,0.1,0])
plt.title("Customized Pie")
plt.show()

# d) Doughnut Chart
plt.pie(recruitment, labels=companies)
circle = plt.Circle((0,0), 0.70, fc='white')
plt.gca().add_artist(circle)
plt.show()

# Comparison IBM vs Amdocs
plt.bar(['IBM', 'Amdocs'], [150, 120])
plt.title("IBM vs Amdocs Recruitment")
plt.show()