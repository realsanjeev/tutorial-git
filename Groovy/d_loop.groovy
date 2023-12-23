for (i in [1,3,4]) {
    println i
}

for (i in 1..5){
    println "i range from 1 to 5: i="+i
}

// upto is also used to loop
1.upto(5) {
    println "From 1 upto " + "$it"
}

// start from 0 to n-1
5.times {
    println "$it times"
}

// step from 1 to 10 in step 2 (upto, step_size)
1.step(10, 2) {
    println "$it step"
}