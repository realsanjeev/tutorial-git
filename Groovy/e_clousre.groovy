// Method using default parameter
def calculateSum(int a, int b = 10) {
    return a + b
}

// Call the method
println "Sum: " + calculateSum(4)

// Closure example
def myClosure = { firstName, lastName ->
    println "Hello, $firstName $lastName"
}

// Call the closure
myClosure.call('RealSanjeev', 'Bhandari')

// Closures are often used to filter or map data in lists or dictionaries
def myList = [42, 1, 2, 43, 2, 4, 53, 213, 1, 3, 3]

// Find returns the element if it finds it, or else null. Now, finding 3:
println 'Find returns the element if found, else null. Now, 3=' + myList.find { item -> item == 3 }

// Return all elements that satisfy the condition:
println 'Return all elements that satisfy the condition: ' + myList.findAll { item -> item > 3 }

// Return true if any element satisfies the condition for at least one element:
println 'Return true if any element satisfies the condition for at least one element: ' + myList.any { item -> item < 3 }
