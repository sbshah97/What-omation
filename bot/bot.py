import aiml
import time

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("eng.xml")

time.sleep(0.5)

print kernel.respond("HI")

# Press CTRL-C to break this loop
while True:
	i = raw_input("# ")
	i = str(i).replace("."," ")
	try:
		s = str(kernel.respond(i))
		s = s.replace("[nl]","\n")
		print("> "+s)
	except:
		print("> ???")