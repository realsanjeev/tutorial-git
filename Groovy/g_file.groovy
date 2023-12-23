String FILE_PATH = 'f_input.groovy'
def fp = new File(FILE_PATH)

println "File: $fp"
println "[TEXT OF FILE]: $fp.text"
println '-'*23
println '[READLINES return the list of lines]: \n' + fp.readLines()
println '-'*23

// collect lines into a list
def list = fp.collect { it }
println "[LIST]: $list"
// store file content in an array
def array = fp as String[]
println "[ARRAY]: $array"

// read file line by line
fp.eachLine {
    line ->
    println "[LINE]: $line"
}

// read file line by line with line no
fp.eachLine {
    line, lineNo ->
    println "$lineNo: $line"
}

// get only specific range line
def lineNoRange = 2..4
def lineList = []
fp.eachLine { line, lineNo ->
    if(lineNoRange.contains(lineNo)) {
        lineList.add(line)
    }
}
for (line in lineList) {
    println "[RANGE LINE]: $line"
}

// read with reader
fp.withReader { reader ->
    // println "[READER]: $reader.readLine()"
    // CHECK FOR eof
    while((line=reader.readLine())!=null) {
        println "line: $line"
    }

}

println '+'*34
/*
* reading with newReader
*/

def outputFile=new File('zOutputFront_g_file.txt')
try {
def reader = fp.newReader()
// println "[READER]: $reader"
// copy content to outputfile

outputFile << reader
reader.close()
} catch (Exception err) {
    println "----===--${err}---====----"
}
// when working with binary files, read content as byte
byte[] contents = fp.bytes
println '[BYTE]: '+ contents[3..10]

// size in bytes
println fp.length()

//check if is a file or dir
println "isFile: ${fp.isFile()} and isDir: ${fp.isDirectory()}"

// delete file 
outputFile.delete()
