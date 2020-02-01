import sys, glob
import aiml

kernel = aiml.Kernel()
kernel.learn("chatFile.xml")

while True: print(kernel.respond(str(input("> "))))