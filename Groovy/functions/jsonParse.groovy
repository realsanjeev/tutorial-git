/*
* JsonSlurper is a class that parses JSON text 
* or reader content into Groovy data structures 
*(objects) such as maps, lists and primitive types 
* like Integer, Double, Boolean and String.
*/

import groovy.json.JsonSlurper;

def jsonSlurper = new JsonSlurper()
def object = jsonSlurper.parseText('{"name": "Groovy", "type":"dynamic"}')

assert object instanceof Map 
assert object.name == 'Groovy'

println "Json Parse: $object"

object = jsonSlurper.parseText '''
{
    "name": "realsanjeev",
    "programing": "python, java",
    "engineer": true,
    "life": 1
}
'''
println "[NEXT]: $object"
