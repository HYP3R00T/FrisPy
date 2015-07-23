#Tom McClintock
#This is the main program for the Frisbee simulator, FrisPy.
#It is simply a small script that combines the rest of
#the parts of the program.

#Import the Animation and MCMC routines
import imp
Animation = imp.load_source("FrisPy_Animation.py","Animation/FrisPy_Animation.py")
MCMC = imp.load_source("FrisPy_MCMC.py","MCMC/FrisPy_MCMC.py")

#Obtain the command line arguments
import sys
argv = sys.argv

#Check if no options have been given
if len(argv)>2 or len(argv)<2:
	message = "Usage error: incorrect number of arguments. Please run with 'python FrisPy [mode]'."
	sys.exit(message)

#Choose either Animation or MCMC, and run in that mode or else throw an error.
mode = argv[1]
if mode.lower() == 'animation':
	print "Running in Animation mode."
	Animation.FrisPy_Animation()
elif mode.lower() == 'mcmc':
	print "Running in MCMC mode."
	MCMC.FrisPy_MCMC()
else:
	message = "Usage Error: incorrect mode. Please specify either 'Animation' or 'MCMC'."
	sys.exit(message)