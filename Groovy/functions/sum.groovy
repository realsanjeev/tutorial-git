def static sum_numbers(...args) {
    def sum = 0
    for (int num in args) {
        sum += num
    }
    return sum
}

static void main(String ...args) {
    // Calling the function with separate arguments
    def result = sum_numbers(1, 2, 3)
    def date = new java.util.Date()
    println "[EXECUTED AT]: ${date}"
    println "Sum of 1, 2, 3: $result"

    println "[INFO]: Groovy closed"
}
