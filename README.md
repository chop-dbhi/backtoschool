# DBHi Back to School Tutorial Curriculum

This an introduction to bioinformatics programming for high school age students. It walks students from a "Hello World" style script to a creating a dynamic webpage to manipulate a medical image. This is not intended as a full introductory course to programming concepts, but rather a view into what is possible. While dated, we've chosen to use a CGI script because it is a very simple way to quickly migrate the students from printing text out to the screen to outputting text to a webpage. This tutorial is intended to run approximately two hours so we have placed an emphasis on simplicity. Each student or team of students can run through the entire tutorial on a Raspberry PI.


# Curriculum Outline

1. Introduce students to the Raspberry PI hardware.
1. Have students navigate to a very simple webpage and "View Source". We can use something like "http://info.cern.ch/", but anything that does not have a lot JavaScript and shows the HTML structure will work.
1. Student's open start.py from this repository
    1. Walk through the contents of this file. It introduces comments and strings.
    1. Have the students add a string to put something within the h1 tag.
    1. Run the script at the console: `./start.py`
    1. Note that nothing happens. Show students they can wrap a print statement around the string. Run again.
    1. Introduce variables and string concatenation to clean up the script and run once more.
    1. Discuss the idea that this script currently prints to the console, but with a few modifications we can cause this content to output to a webpage.
    1. Uncomment the two print statements on lines 9 and 10. This is just to support CGI protocol
    1. Tell the students to execute the server.py script `./server.py`
    1. Have the students open a web browser and navigate to http://localhost:8000/start.py. Let them play with this for a bit
1. Switch over to the portal.py script. 
	1. Explain this is effectively the same with a few minor additions to support our next task.
	1. Briefly run through the script explaining new concepts.
	1. With server.py still running, have students navigate to http://localhost:8000/portal.py

# TODO 
Continue developing portion of project where students and zoom/filter capability to the webpage


# TODO
Add a list of "next level" resources for students looking to go further

