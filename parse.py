from optparse import OptionParser

parser = OptionParser()

parser.add_option('-f', "--file", type="string", action="store" , dest="filename")

args = ["-f", "foo.txt"]
(options, ars) = parser.parse_args(args)

print("These are %s and also %s are arguments" % (options, args))
