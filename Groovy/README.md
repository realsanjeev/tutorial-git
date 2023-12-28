# Groovy
Groovy is a powerful, dynamic, and object-oriented programming language designed for the Java Virtual Machine (JVM). It shares similarities with Java but incorporates features from other languages like Python, Ruby, and Smalltalk. Groovy is often referred to as a scripting language for the Java platform.

[All syntaxt and method valid in jav is also vaild in groovy.]
## Installation
> For Updated info: Go to [Official website](https://groovy-lang.org/documentation.html)

**Window**
Install using [Window installer](https://groovy.apache.org/download.html)

**Linux**
Install using SDKMAN! (The Software Development Kit Manager)

```bash
curl -s get.sdkman.io | bash
```

Locate the sdkman installation directory:

```bash
whereis sdkman-init.sh
```

The output will be similar to: `sdkman-init: /usr/local/sdkman/bin/sdkman-init.sh`

Activate sdkman:

```bash
source "/usr/local/sdkman/bin/sdkman-init.sh"
```

Now, install the latest stable version of Groovy:

```bash
sdk install groovy
```

## Installation Check

To check if Groovy is installed, use the following command. Ensure that environment variables are set up if not done by default during installation.

```bash
groovy --version
```

To find the path of the Groovy installation, you can use the following command in (window):

```bash
where groovy
```
In linux(github-codespace):
```bash
whereis groovy
```

## Run the Groovy file
Groovy file has `.groovy` extension. To run groovy program
```bash
groovy <file_name>
```

## Key characteristics and features of Groovy

1. **Syntax:** Groovy has a concise and expressive syntax, making it easy to read and write. It eliminates much of the boilerplate code that is common in Java, which can lead to more productive development.

2. **Dynamic Typing:** Groovy is dynamically typed, meaning that variable types are determined at runtime. This allows for more flexibility in coding and can lead to shorter and more readable code.

3. **Closures:** Groovy supports closures, which are blocks of code that can be passed around and executed later. Closures enable concise and expressive coding patterns, facilitating the use of functional programming concepts.

4. **DSL Support:** Groovy is often used to create Domain-Specific Languages (DSLs). Its syntax is flexible enough to allow developers to create DSLs that are tailored to specific problem domains, making the code more readable and expressive.

5. **Integration with Java:** Groovy can seamlessly integrate with existing Java code. This means that Java libraries can be used directly in Groovy code, and Groovy code can be used in Java projects.

6. **Scripting Capabilities:** While Groovy is a fully compiled and statically-typed language, it also supports scripting. Developers can write scripts quickly without the need for a compilation step, making it suitable for rapid development and automation tasks.

### Use Cases and Why Groovy is Needed:

1. **Scripting on the JVM:** Groovy provides a convenient and expressive scripting language for the Java platform. It allows developers to leverage the vast ecosystem of Java libraries and tools while enjoying a more concise syntax.

2. **Build Automation:** Groovy is often used in build tools like Apache Groovy (formerly known as Gradle) and Apache Ant. Its concise syntax makes it well-suited for writing build scripts, making the build process more maintainable and readable.

3. **Testing:** Groovy is commonly used in testing frameworks, such as Spock, for writing concise and expressive test specifications.

4. **Rapid Prototyping:** The dynamic nature of Groovy makes it suitable for rapid prototyping and experimentation. Developers can quickly iterate over ideas without the need for extensive compilation and boilerplate code.

5. **Domain-Specific Languages (DSLs):** Groovy's flexibility and expressive syntax make it an excellent choice for creating DSLs tailored to specific application domains, enhancing readability and maintainability.

## Data Types in Groovy

Groovy's data types are similar to those in Java. The basic data types include:

- `byte`
- `short`
- `int`
- `long`
- `float`
- `double`
- `String`
- `Boolean`

Here's an example demonstrating the use of data types and initializing variables:

```groovy
// Using 'def' to define a variable without specifying the data type explicitly
def b = 32

// Typecasting when initializing the variable
def b = (byte) 32
// or
byte b = 32

// Print the value of the variable
println b // -> 32

// To see the range of numeric data types
println Byte.MIN_VALUE
println Byte.MAX_VALUE
```

**Strings:**

- Single quotes (`''`) and triple single quotes (`''' '''`) do not support interpolation. Single quotes are used for single-line input.

- Double quotes (`""`) and triple double quotes (`""" """`) support interpolation.

- `/ /` (slashy) and `$/ /$` (dollar slashy) are used to represent strings within. Both support interpolation and multiline. They are commonly used for regex expressions since they don't change the string (i.e., escape characters cannot be autoescaped).


## Operators
All the operator available in java is available in `groovy``. Except java operator we have `.intdiv()` for integer division, `**` for power. To check validity of operation we  use `assert`. It only gives error when statement give false.
```
assert 3+4==7 
```
### Conditional and Loop operator
we can write he expression to evaluate in switch `case` inside the curly bracket:
```case {x>0}:
    statement; break;
```


There is `for each` loop in groovy

## Methods and Closures in Groovy

### Methods:

In Groovy, methods can be defined, and unlike Java, default parameters can be specified. Here's an example:

```groovy
def sum(int q = 3, int p = 10) {
    return q + p
}

// Call the method
println sum(4, 2) // -> 6
```

### Closures:

Closures in Groovy are blocks of code that can take parameters, reference variables, return values, and can be passed as parameters in a method.

They differ from methods in that they can reference variables from outside the closure, which is not possible in a method. Closures can be called using the `.call()` method. Here's an example:

```groovy
def str = "Hello"

// We can pass the variable using ->
def myClosure = { name -> println "$str $name" }
myClosure.call("Real Sanjeev")
```

Closures provide a flexible way to encapsulate functionality and can be particularly useful for tasks like defining callbacks or passing behavior as a parameter to a method. The ability to reference external variables makes closures a powerful construct in Groovy programming.

## Lists in Groovy

In Groovy, lists share some similarities with Python lists. Here are some key points about lists in Groovy:

- You can access the last element of a list using `[-1]`.

- To access a slice of elements, you can use the range syntax. For example, `[0..3]` corresponds to elements at indices 0, 1, 2, and 3. This is similar to the Python syntax `[0:4]`.

- The `.contains` method is used to check if an element is present in the list.

- To append an element to a list, you can use the `.add` method or the `<<` operator. For example, `myList << "element"` adds the element to the end of the list.

Here's a brief example demonstrating these concepts:

```groovy
// Creating a list
def myList = [1, 2, 3, 4, 5]

// Accessing the last element
def lastElement = myList[-1]

// Accessing a slice of elements
def sliceOfElements = myList[0..3]

// Checking if an element is in the list
def containsElement = myList.contains(3)

// Appending an element to the list
myList << 6

// Displaying the results
println "Last Element: $lastElement"
println "Slice of Elements: $sliceOfElements"
println "Contains Element 3: $containsElement"
println "Updated List: $myList"
println myList.reverse() + myList.sort() + myList.isEmpty()
```
## Maps
Key value pair collection type
[key: value]
```
def emp = [
    'name':'San', age:23
]
println emp
println emp.name + "is same as " + emp['name] + emp.get('name')
println emp.containsKey('name) + emp.containsValues('San')
```

### Ranges
Create a list of sequential value
denoted by first and last value of sequence
1..10, 'a'..'z', 10..1

Types of range: inclusive and exclusive
1..10  includes 1 to 10
1..<10  includes 1 to 9(exclude 10)
```java
def range = 1..10
println range // 1..10
println range.size() //10
println range.getFrom() // 1
println range.getTo() //10
println range.get(3) + range[3]
def  range2 = range.subList(3,6) // createeed new range
println range instanceof java.util.List;
```

### **RegEX**
Regex is simply a petterns used to find the substring in a text.
`~` sign is followed by regex expression

```java
// returns null if expression not found
def match "Groovy" =~ "Groovy"
if (match) {
    println match[0]
}
```

> To use the function from other file, we can use as class usage just like java. Otherwise we need static function to make it work.