
String mainText = '''This is a text fror multiple line.
This is line 1
This is line 2
This is line last'''

println mainText

println '-'*21
def match= mainText=~'This'
if (match) {
    println "[matched object]: $match"
    // show all the match
    for (m in match) {
        println "[MATCH]: ${m}"
    }
} else {
    println 'Match not found'
}
