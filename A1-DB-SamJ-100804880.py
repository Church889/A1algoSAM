
#Samuel. M. Joseph
#100804880
#Submission date: 07/09/2024
#Algorithms & Data Structures

import time
import sys

# Step 1: Loading and storing the product data
class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.price}, {self.category})"

#load product date
def loadPD(path):
    products = []
    #r used to initiate read for the file.
    with open(path, 'r') as file:
        for line in file:
            product_id, name, price, category = line.strip().split(', ')
            products.append(Product(int(product_id), name, float(price), category))
    print("Loaded products:", products)  
    return products

# Save product data 
def savePD(products,path):
    #w used to initiate write for the file.
    with open(path, 'w') as file:
        for product in products:
            line = f"{product.product_id}, {product.name}, {product.price}, {product.category}\n"
            file.write(line)
    print("SAVED WRITES")  

# Step 2: Insert,update,load,save etc.
def insertPD(products, product, path):
    products.append(product)
    print("Inserted product:", product)  
    savePD(products, path)

# Update products
def updatePD(products,product_id, path,name=None, price=None, category=None):
    for product in products:
        if product.product_id == product_id:
            if name is not None:
                product.name = name
            if price is not None:
                product.price = price
            if category is not None:
                product.category = category
            print("UPDATED", product)  
            savePD(products, path)
            return True
    print("NULL ID")  #IF id doesn't exist 
    return False

# Search products
def searchPD(products, key, value):
    result = []
    for product in products:
        if getattr(product, key) == value:
            result.append(product)
    return result

# Delete products    
def deletePD(products, product_id, path):
    originalLen= len(products)
    products[:]= [product for product in products if product.product_id != product_id]
    
    if len(products)<originalLen:
        print("Deleted product with ID: ", product_id)  
        savePD(products, path)
        return True
    print("NO ID FOUND")  

#bubble sort
def bubbleSort(products):
    n=len(products)
    swapped=True
    while swapped:
        swapped=False
        for i in range(1,n):
            if products[i-1].price>products[i].price:
                products[i-1],products[i]=products[i],products[i-1]
                swapped=True
              



    
def measureTime(products, sortFunction):
    start=time.perf_counter()
    sortFunction(products)
    end=time.perf_counter()
    return 1000 * (end-start)  #millisecondss
#path for txt
path='C:\\product_data.txt'

#load products data
products=loadPD(path)

#update price of first row of data
updatePD(products,57353,path,price=1337.00)
deletePD(products,40374,path)

#print updated products
print("UPDATED")
for product in products:
    print(product)

# Sorting products by price using Bubble Sort
bubbleSort(products)
print("Sorted Products by Price:")
for product in products:
    print(product)



# Prepare different cases for sorting
sortedProducts = sorted(products, key=lambda p: p.price)
reverseProducts = sorted(products, key=lambda p: p.price, reverse=True)


# Measure sort times
sortedTime = measureTime(sortedProducts[:], bubbleSort)
reverseTime = measureTime(reverseProducts[:], bubbleSort)
averageTime = (sortedTime+reverseTime/2)



# Print sort times
print(f"BEST:  Already sorted: {sortedTime:.6f} ms")
print(f"WORST: Reverse Sorted {reverseTime:.6f}ms")
print(f"AVGs time: {averageTime:6f} ms")

# Print time complexities
print("--TIME COMPLEXITY--")
print("BEST : O(n) when already sorted")
print("AVG : O(n^2)")
print("WORST : O(n^2) for reverse order")

#used modules and some references that will be in the paper provided.

