// Groovy is a dynamically typed language
def name = "RealSanjeev"

// It outputs: Well done RealSanjeev
// Use double quotes for string interpolation
println "Well done '${name}'"

// It outputs: Well done ${name}
// Single quotes do not perform string interpolation
println 'Well done "${name}"'
/*
* assign values in list to variable
* we can also define the datatypes
* and typecast if donot match the type if possible
* ie int can be cast into str and float
* but str cannot be converted into int. It raises the error
*/
def (String a, int b) = ["This is string first ", 30.43]
println a + b

def arr = (1..10).toArray()
println arr