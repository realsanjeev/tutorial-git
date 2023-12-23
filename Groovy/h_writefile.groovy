File myFile = new File('data.txt')

myFile.write('This is Line1\n')
myFile << 'This is Line2'

String name = 'RealSanjeev'
// myFile.text = "This override the content of file $name"
println myFile.text

myFile.withWriter { writer ->
    writer.writeLine('This is Line4')
}
myFile.append("\nThis is Line 5 from $name")
println "Length of file: ${myFile.length()}"
/* groovylint-disable-next-line UnnecessaryGetter */
println "${myFile} is file: ${myFile.isFile()} and is dir: ${myFile.isDirectory()} and is hidden: ${myFile.isHidden()}"

def newFile = new File('data2.txt')
newFile << myFile.text

// rename the file
newFile.renameTo(new File("renamed.txt"))
