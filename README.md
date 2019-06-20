# Devanagari
Handwriting recognition - Identifies the user input as one of the letters of the devanagari script.
First the model is built and trained, then the application is run to check the results. 

Hardware Information

OS Name	Microsoft Windows 10 Home Version	10.0.17134 Build 17134 System Type	x64-based PC Processor	Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz, 2904 Mhz, 2 Core(s), 4 Logical Processor(s) BIOS Mode	UEFI

Dataset
After splitting the dataset into training and testing data we get:
no.of training examples:70000

no.of testing examples:2000

X_train shape:(70000, 1024)

Y_train shape:(1, 70000)

X_test shape:(2000, 1024)

Y_test shape:(1, 2000)


The script file for the project is build_model.py, devanagari_application.py. build_model comprises of building the model, training and testing the data. devanagari_application concerns with getting the final result as recognising the handwriting as one of the letters of devanagari script. 
